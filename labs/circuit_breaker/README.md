# Circuit Breaker

## Question

Why should a system sometimes stop calling a dependency instead of retrying forever?

## Smallest experiment

After several consecutive failures, the breaker changes:

```text
CLOSED → OPEN
```

and rejects further requests.

A success resets it in this minimal model.

## Why it matters

This pattern helps prevent cascading failures in:

- APIs
- robot cloud services
- dependent subsystems
- external sensors/services

## Run

```bash
python labs/circuit_breaker/circuit_breaker.py
```

## Test angle

Verify:

- the breaker opens at the threshold;
- it stays closed before the threshold;
- success resets failure count.
