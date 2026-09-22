"""Minimal exponential-backoff experiment."""

def delay_seconds(attempt: int, base: float = 0.5, cap: float = 8.0) -> float:
    if attempt < 1:
        raise ValueError("attempt must be >= 1")
    return min(base * (2 ** (attempt - 1)), cap)

if __name__ == "__main__":
    print("retry attempt -> delay")
    for attempt in range(1, 8):
        print(f"{attempt:>2} -> {delay_seconds(attempt):>4.1f}s")
