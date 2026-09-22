# Heartbeat Watchdog

## Question

How can a tester detect that a robot component has silently stopped reporting health?

## Smallest experiment

A component periodically sends a heartbeat. If the latest heartbeat is older than a timeout threshold, the watchdog marks it as stale.

## Why it matters

This pattern appears in:

- robot controllers
- sensors
- distributed services
- network clients
- health monitoring

## Run

```bash
python labs/heartbeat_watchdog/watchdog.py
```

## Test angle

Useful checks include:

- exactly on the timeout boundary;
- just below the timeout;
- just above the timeout;
- invalid timeout values.
