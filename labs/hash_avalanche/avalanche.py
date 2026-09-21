"""Visualize the avalanche effect of SHA-256."""
from __future__ import annotations
import hashlib

def sha256_bits(text: str) -> str:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return "".join(f"{byte:08b}" for byte in digest)

def bit_difference(left: str, right: str) -> int:
    return sum(a != b for a, b in zip(left, right))

def compare(left: str, right: str) -> tuple[int, float]:
    a, b = sha256_bits(left), sha256_bits(right)
    changed = bit_difference(a, b)
    return changed, changed / len(a)

if __name__ == "__main__":
    pairs = [
        ("curiosity", "Curiosity"),
        ("hello world", "hello worle"),
        ("123456", "123457"),
    ]
    for left, right in pairs:
        changed, ratio = compare(left, right)
        print(f"{left!r} -> {right!r}")
        print(f"changed bits: {changed}/256 ({ratio:.1%})")
        print("-" * 42)
