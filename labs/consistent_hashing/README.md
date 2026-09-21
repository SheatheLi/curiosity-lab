# Consistent hashing

Distributed systems often need to decide which node owns a key.

If the node count changes, naïve modulo hashing can move many keys. Consistent hashing is designed to reduce that movement.

```bash
python labs/consistent_hashing/consistent_hash.py
```

This tiny implementation uses virtual replicas to make distribution smoother.
