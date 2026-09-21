# Hash avalanche

Change one character and compare the 256 output bits of SHA-256.

A cryptographic hash is designed so that a small input change produces a large, unpredictable output change.

```bash
python labs/hash_avalanche/avalanche.py
```

Look for a changed-bit ratio around half the output bits. Exact values vary by input pair.
