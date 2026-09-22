# Engineering log

## 2026-09-21

Repository initialized.

Initial experiments:
- SHA-256 avalanche effect
- Bloom filter
- Birthday paradox
- Tiny TF-IDF search
- Consistent hashing

The goal is not to make each experiment large. The goal is to turn curiosity into runnable evidence.
## 2026-09-22

Added `retry_backoff`, a minimal experiment showing exponential retry backoff with a maximum delay cap.

Connection to reliability testing:

- repeated failures should not trigger uncontrolled rapid retries;
- retry policy changes system timing and recovery behavior;
- tests should verify attempt count, delay growth, cap behavior, and eventual recovery/failure.
## 2026-09-22

Added five reliability-oriented curiosity labs:

- `heartbeat_watchdog` â€?stale component detection
- `timeout_budget` â€?end-to-end deadline budgeting
- `idempotency_guard` â€?safe duplicate request handling
- `circuit_breaker` â€?stop repeated calls after failures
- `token_bucket` â€?simple request rate limiting

These experiments connect software reliability ideas to robot/system-test thinking:
observe state, define boundaries, inject failures, verify recovery and prevent uncontrolled repeated actions.
