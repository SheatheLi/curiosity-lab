# Timeout Budget

## Question

Why can a workflow still exceed its expected duration even when every individual step has its own timeout?

## Smallest experiment

Track a **single total deadline budget** across multiple sequential steps.

## Why it matters

In robot task execution, an overall mission may contain:

- navigation;
- perception;
- action;
- confirmation.

Testing only per-step timeout can miss end-to-end deadline violations.

## Run

```bash
python labs/timeout_budget/timeout_budget.py
```

## Test angle

Check:

- remaining time decreases correctly;
- budget never becomes negative;
- exact exhaustion returns zero.
