"""A tiny Bloom filter implemented with only the standard library."""
from __future__ import annotations
import hashlib

class BloomFilter:
    def __init__(self, size: int = 128, hash_count: int = 3):
        if size <= 0 or hash_count <= 0:
            raise ValueError("size and hash_count must be positive")
        self.size = size
        self.hash_count = hash_count
        self.bits = 0

    def _indexes(self, item: str):
        raw = item.encode("utf-8")
        for i in range(self.hash_count):
            digest = hashlib.blake2b(raw, digest_size=8, person=f"bf{i}".encode()).digest()
            yield int.from_bytes(digest, "big") % self.size

    def add(self, item: str) -> None:
        for idx in self._indexes(item):
            self.bits |= 1 << idx

    def __contains__(self, item: str) -> bool:
        return all(self.bits & (1 << idx) for idx in self._indexes(item))

if __name__ == "__main__":
    bloom = BloomFilter(size=64, hash_count=3)
    inserted = ["python", "redis", "docker", "spring"]
    for word in inserted:
        bloom.add(word)

    for word in inserted + ["rust", "kafka", "robotics"]:
        verdict = "probably present" if word in bloom else "definitely absent"
        print(f"{word:10} -> {verdict}")
