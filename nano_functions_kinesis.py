import json
import time
import re
import boto3
import requests
from datetime import datetime, timezone

REGION = "us-east-1"
MASTODON_SECRET_ID = "API-KEY-MASTODON"
STREAM_NAME = "mastodont-intake"

# Elige UNA fuente:
MODE = "public"
HASHTAG = "spain"        # usado si MODE="hashtag"

POLL_SECONDS = 20
LIMIT = 100               # posts por pull

s = boto3.client("secretsmanager", region_name=REGION)
kinesis = boto3.client("kinesis", region_name=REGION)

_html = re.compile(r"<.*?>")

def strip_html(text: str) -> str:
    return re.sub(_html, "", text or "").strip()

def get_secret():
    resp = s.get_secret_value(SecretId=MASTODON_SECRET_ID)
    return json.loads(resp["SecretString"])

def fetch_statuses(base_url, token, since_id=None):
    headers = {"Authorization": f"Bearer {token}"}
    params = {"limit": LIMIT}
    if since_id:
        params["since_id"] = since_id

    if MODE == "public":
        url = f"{base_url}/api/v1/timelines/public"
    else:
        url = f"{base_url}/api/v1/timelines/tag/{HASHTAG}"

    r = requests.get(url, headers=headers, params=params, timeout=30)
    return r

def main():
    cfg = get_secret()
    base_url = cfg["MASTODON_BASE_URL"].rstrip("/")
    token = cfg["API-Mastodon"]

    since_id = None
    backoff = 5

    print(f"[INFO] Mastodon producer started. mode={MODE} hashtag={HASHTAG} every={POLL_SECONDS}s")

    while True:
        try:
            r = fetch_statuses(base_url, token, since_id)

            if r.status_code == 429:
                print("[WARN] Mastodon rate limit (429). Sleeping 60s.")
                time.sleep(60)
                continue

            if r.status_code != 200:
                print(f"[ERROR] HTTP {r.status_code}: {r.text[:200]}")
                time.sleep(backoff)
                backoff = min(backoff * 2, 120)
                continue

            backoff = 5
            statuses = r.json()

            # Mastodon devuelve orden por "más reciente primero" normalmente.
            # Para avanzar since_id: nos quedamos con el máximo "id" visto.
            max_id = since_id
            sent = 0

            for st in statuses:
                st_id = st.get("id")
                if st_id and (max_id is None or int(st_id) > int(max_id)):
                    max_id = st_id

                text = strip_html(st.get("content", ""))
                if not text:
                    continue

                event = {
                    "source": "mastodon",
                    "id": st_id,
                    "created_at": st.get("created_at"),
                    "lang": st.get("language"),
                    "text": text,
                    "acct": (st.get("account") or {}).get("acct"),
                    "url": st.get("url"),
                    "tags": [t.get("name") for t in (st.get("tags") or []) if t.get("name")],
                    "ingest_ts": datetime.now(timezone.utc).isoformat()
                }

                kinesis.put_record(
                    StreamName=STREAM_NAME,
                    Data=(json.dumps(event) + "\n").encode("utf-8"),
                    PartitionKey=st_id or str(int(time.time()))
                )
                sent += 1

            since_id = max_id
            print(f"[INFO] Pulled={len(statuses)} sent={sent} since_id={since_id}")

            time.sleep(POLL_SECONDS)

        except Exception as e:
            print(f"[WARN] Error: {e}")
            time.sleep(backoff)
            backoff = min(backoff * 2, 120)

if __name__ == "__main__":
    main()