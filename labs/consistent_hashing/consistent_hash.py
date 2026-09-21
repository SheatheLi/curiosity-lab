"""A compact consistent-hashing ring experiment."""
from __future__ import annotations
import bisect
import hashlib

def h(value: str) -> int:
    return int.from_bytes(hashlib.sha256(value.encode()).digest()[:8], "big")

class HashRing:
    def __init__(self, nodes=(), replicas: int = 40):
        self.replicas = replicas
        self.points: list[int] = []
        self.owners: dict[int, str] = {}
        for node in nodes:
            self.add(node)

    def add(self, node: str) -> None:
        for replica in range(self.replicas):
            point = h(f"{node}:{replica}")
            bisect.insort(self.points, point)
            self.owners[point] = node

    def get(self, key: str) -> str:
        if not self.points:
            raise LookupError("ring is empty")
        point = h(key)
        idx = bisect.bisect_left(self.points, point)
        if idx == len(self.points):
            idx = 0
        return self.owners[self.points[idx]]

def assignments(nodes, keys):
    ring = HashRing(nodes)
    return {key: ring.get(key) for key in keys}

if __name__ == "__main__":
    keys = [f"user:{i}" for i in range(1000)]
    before = assignments(["A", "B", "C"], keys)
    after = assignments(["A", "B", "C", "D"], keys)
    moved = sum(before[k] != after[k] for k in keys)
    print(f"keys moved after adding D: {moved}/{len(keys)} ({moved/len(keys):.1%})")
    print("A naive modulo-based scheme often remaps a much larger fraction.")
