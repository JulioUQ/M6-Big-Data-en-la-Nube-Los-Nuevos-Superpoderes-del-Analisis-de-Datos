import json
import time
import urllib.request
import urllib.error
import boto3
from datetime import datetime, timezone
from urllib.parse import unquote_plus
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
sm = boto3.client("secretsmanager", region_name="us-east-1")

# Hugging Face
HF_SECRET_ID = "API-Key-HuggingFace"
HF_MODEL_ID = "tabularisai/multilingual-sentiment-analysis"
HF_MODEL_URL = f"https://router.huggingface.co/hf-inference/models/{HF_MODEL_ID}"

# S3
RAW_PREFIX = r"rawdata/"
PROCESSED_PREFIX = r"processeddata/"

def get_hf_token():
    sec = sm.get_secret_value(SecretId=HF_SECRET_ID)
    sec_json = json.loads(sec["SecretString"])
    return sec_json["AWS-model_uoc"]

def hf_call(token: str, text: str, retries: int = 6):
    payload = json.dumps({
    "inputs": text,
    "parameters": {
        "truncation": True,
        "max_length": 512
    }
    }).encode("utf-8")


    for i in range(retries):
        try:
            req = urllib.request.Request(
                HF_MODEL_URL,
                data=payload,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                },
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))

        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            if e.code in (429, 503, 500, 502, 504):
                sleep_s = min(2 ** i, 30)
                print(f"[WARN] HF HTTP {e.code}. retry in {sleep_s}s. body={body[:120]}")
                time.sleep(sleep_s)
                continue
            raise RuntimeError(f"HF HTTPError {e.code}: {body[:300]}")

    raise RuntimeError("HF retries exhausted")

def pick_top_label(pred):
    # Posibles formatos:
    # - [{"label": "...", "score": ...}, ...]
    # - [[{...},{...}]] (lista anidada)
    if isinstance(pred, list) and pred and isinstance(pred[0], list):
        pred = pred[0]

    if isinstance(pred, list) and pred:
        best = max(pred, key=lambda x: x.get("score", 0))
        return best.get("label"), best.get("score"), pred

    return None, None, pred

def get_object_with_retries(bucket: str, key: str, attempts: int = 6):
    for i in range(attempts):
        try:
            return s3.get_object(Bucket=bucket, Key=key)
        except ClientError as e:
            code = e.response.get("Error", {}).get("Code", "")
            if code == "NoSuchKey":
                sleep_s = 1 + i
                print(f"[WARN] NoSuchKey {key}. retry in {sleep_s}s")
                time.sleep(sleep_s)
                continue
            raise
    raise RuntimeError(f"Object not found after retries: s3://{bucket}/{key}")

def lambda_handler(event, context):
    hf_token = get_hf_token()

    for rec in event.get("Records", []):
        bucket = rec["s3"]["bucket"]["name"]
        key = unquote_plus(rec["s3"]["object"]["key"])

        print(f"[INFO] Event bucket={bucket} key={key}")

        if not key.startswith(RAW_PREFIX) or not key.endswith(".jsonl"):
            print(f"[INFO] Skipping key={key}")
            continue

        obj = get_object_with_retries(bucket, key)
        content = obj["Body"].read().decode("utf-8")

        out_lines = []
        for line in content.splitlines():
            if not line.strip():
                continue
            data = json.loads(line)

            text = (data.get("text") or "")[:2000]
            pred = hf_call(hf_token, text)
            label, score, full = pick_top_label(pred)

            enriched = {
                **data,
                "sentiment": label,
                "sentiment_score": score,
                "sentiment_full": full,
                "processed_ts": datetime.now(timezone.utc).isoformat(),
                "sentiment_engine": "hf/tabularisai/multilingual-sentiment-analysis",
            }
            out_lines.append(json.dumps(enriched))

        # processed/dt=.../batch_....jsonl
        processed_key = key.replace(RAW_PREFIX, PROCESSED_PREFIX, 1)

        s3.put_object(
            Bucket=bucket,
            Key=processed_key,
            Body=("\n".join(out_lines) + "\n").encode("utf-8"),
            ContentType="application/json",
        )

        print(f"[INFO] Wrote processed_key={processed_key} lines={len(out_lines)}")

    return {"status": "ok"}
