# curiosity-lab

A small collection of runnable experiments for ideas that are easier to understand by touching them.

The rule is simple:

> **See something interesting → build the smallest experiment → run it → record what changed in my understanding.**

This repository is intentionally lightweight. Each lab should be small enough to read quickly and concrete enough to run locally.

Current experiments span small algorithms, data structures, search, distributed systems, and reliability engineering.

---

## Labs

### Foundations & Algorithms

| Lab | Question |
| --- | --- |
| `hash_avalanche` | How much can one tiny input change alter a SHA-256 hash? |
| `bloom_filter` | How can a data structure answer “probably present / definitely absent” with very little memory? |
| `birthday_paradox` | Why does a shared birthday become likely with surprisingly few people? |
| `tiny_search` | How can a tiny TF-IDF search engine rank text without a search server? |
| `consistent_hashing` | Why is consistent hashing useful when nodes join or leave a distributed system? |

### Reliability & System Behavior

| Lab | Question |
| --- | --- |
| `retry_backoff` | Why should retries slow down instead of firing continuously? |
| `heartbeat_watchdog` | How can a system detect that a component has silently stopped reporting health? |
| `timeout_budget` | How can an end-to-end workflow share one total deadline? |
| `idempotency_guard` | What should happen when the same request is sent more than once? |
| `circuit_breaker` | When should a system stop calling a failing dependency? |
| `token_bucket` | How can a system limit request rate and protect itself from overload? |

---

## Run

Python 3.10+ is enough. No third-party dependencies are required.

### Foundations & Algorithms

```bash
python labs/hash_avalanche/avalanche.py
python labs/bloom_filter/bloom_filter.py
python labs/birthday_paradox/simulate.py
python labs/tiny_search/tfidf_search.py
python labs/consistent_hashing/consistent_hash.py
```

### Reliability & System Behavior

```bash
python labs/retry_backoff/retry_backoff.py
python labs/heartbeat_watchdog/watchdog.py
python labs/timeout_budget/timeout_budget.py
python labs/idempotency_guard/idempotency_guard.py
python labs/circuit_breaker/circuit_breaker.py
python labs/token_bucket/token_bucket.py
```

---

## Tests

Run all tests:

```bash
python -m unittest discover -s tests -v
```

The tests are intentionally small. Their purpose is to make each experiment's key behavior explicit and easy to verify.

---

## Lab Format

Each experiment aims to contain:

- a narrow question;
- the smallest useful implementation;
- a visible result;
- a short explanation of why the behavior matters;
- at least one testing or failure-oriented observation when useful.

A reusable starter is available in:

```text
LAB_TEMPLATE.md
```

---

## Engineering Log

`ENGINEERING_LOG.md` records how the repository grows over time.

The point is not to make every experiment large.

The point is to leave a trace of:

```text
curiosity
→ experiment
→ execution
→ observation
→ understanding
```

---

## Current Direction

The repository is intentionally open-ended, but the current reliability cluster focuses on ideas such as:

```text
retry
timeout
heartbeat
idempotency
circuit breaking
rate limiting
```

These concepts appear in APIs, distributed systems, fault recovery, service reliability, and robot/system testing.

They are useful because they turn abstract reliability ideas into small behaviors that can actually be executed, observed, and tested.

---

## Status

This is a living curiosity repository.

Small experiments are welcome.

Perfection is not required; each lab should simply make one idea more concrete than it was before.
