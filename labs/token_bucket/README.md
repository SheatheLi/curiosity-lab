# Token Bucket

## Question

How can a system limit how quickly requests are accepted?

## Smallest experiment

A bucket starts with a limited number of tokens. Each request consumes one token.

If no token remains, the request is rejected until the bucket is refilled.

## Why it matters

Rate limiting can protect:

- APIs
- telemetry ingestion
- command gateways
- overloaded services

## Run

```bash
python labs/token_bucket/token_bucket.py
```

## Test angle

Check:

- requests consume tokens;
- empty bucket rejects;
- refill never exceeds capacity.
