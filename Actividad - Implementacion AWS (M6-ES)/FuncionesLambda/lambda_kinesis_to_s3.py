import json
import base64
import boto3
from datetime import datetime, timezone

s3 = boto3.client("s3")

BUCKET = "buquet-mastodon-data"   
RAW_PREFIX = "rawdata/"             

def lambda_handler(event, context):
    records = []

    for record in event["Records"]:
        payload = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")

        
        data = json.loads(payload)
        records.append({
            **data,
            "raw_ingest_ts": datetime.now(timezone.utc).isoformat()
        })

    if not records:
        return {"stored": 0}

    key = (
        RAW_PREFIX
        + f"dt={datetime.utcnow().date()}/"
        + f"batch_{context.aws_request_id}.jsonl"
    )

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=("\n".join(json.dumps(r) for r in records) + "\n").encode("utf-8"),
        ContentType="application/json"
    )

    return {"stored": len(records), "s3_key": key}
