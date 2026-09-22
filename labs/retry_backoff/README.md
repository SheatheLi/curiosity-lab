# Retry Backoff

## Question

Why shouldn't a client retry a failed operation immediately and repeatedly?

## Smallest experiment

This lab implements **exponential backoff**:

- retry 1 → 0.5 s
- retry 2 → 1.0 s
- retry 3 → 2.0 s
- retry 4 → 4.0 s
- retry 5+ → capped at 8.0 s

## Why it matters

Immediate retries can make an overloaded or temporarily unavailable system even worse.

Backoff spaces retries out so the system gets time to recover.

This idea appears in API clients, distributed systems, robot task execution,
network reconnect logic, and fault recovery.

## Run

```bash
python labs/retry_backoff/retry_backoff.py
```

## Next curiosity

Real systems often add **jitter** so many clients do not retry at the same moment.
