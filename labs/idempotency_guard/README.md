# Idempotency Guard

## Question

What should happen if the same request is sent twice?

## Smallest experiment

This lab stores the first payload associated with an idempotency key.

Then:

- same key + same payload → safe duplicate;
- same key + different payload → conflict.

## Why it matters

Retries are common in unreliable networks. Without idempotency, a repeated request may execute the same robot task twice.

## Run

```bash
python labs/idempotency_guard/idempotency_guard.py
```

## Connection

This directly connects to system testing of:

- retry;
- duplicate requests;
- exactly-once-like behavior;
- database state consistency.
