"""A tiny token-bucket rate limiter without wall-clock time."""

class TokenBucket:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        self.capacity = capacity
        self.tokens = capacity

    def allow(self, cost: int = 1) -> bool:
        if cost < 1:
            raise ValueError("cost must be >= 1")
        if self.tokens < cost:
            return False
        self.tokens -= cost
        return True

    def refill(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.tokens = min(self.capacity, self.tokens + amount)


if __name__ == "__main__":
    bucket = TokenBucket(capacity=3)

    for i in range(5):
        print(f"request {i + 1}: allow={bucket.allow()} tokens={bucket.tokens}")

    bucket.refill(2)
    print(f"after refill: tokens={bucket.tokens}")
