# curiosity-lab

A small collection of runnable experiments for ideas that are easier to understand by touching them.

The rule is simple:

> **See something interesting → build the smallest experiment → run it → record what changed in my understanding.**

This repository is intentionally lightweight. Each lab should be small enough to read quickly and concrete enough to run locally.

## Labs

| Lab | Question |
| --- | --- |
| `hash_avalanche` | How much can one tiny input change alter a SHA-256 hash? |
| `bloom_filter` | How can a data structure answer “probably present / definitely absent” with very little memory? |
| `birthday_paradox` | Why does a shared birthday become likely with surprisingly few people? |
| `tiny_search` | How can a tiny TF-IDF search engine rank text without a search server? |
| `consistent_hashing` | Why is consistent hashing useful when nodes join or leave a distributed system? |

## Run

Python 3.10+ is enough. No third-party dependencies are required.

```bash
python labs/hash_avalanche/avalanche.py
python labs/bloom_filter/bloom_filter.py
python labs/birthday_paradox/simulate.py
python labs/tiny_search/tfidf_search.py
python labs/consistent_hashing/consistent_hash.py
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Lab format

Each experiment aims to contain:

- a narrow question;
- a runnable implementation;
- a visible result;
- a short note about what the result means.

## Status

This is a living curiosity repository. Small experiments are welcome; perfection is not required.
