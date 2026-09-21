"""Monte Carlo simulation of the birthday paradox."""
from __future__ import annotations
import random

def has_collision(group_size: int, days: int = 365) -> bool:
    birthdays = [random.randrange(days) for _ in range(group_size)]
    return len(set(birthdays)) != len(birthdays)

def estimate(group_size: int, trials: int = 20_000, seed: int = 42) -> float:
    random.seed(seed)
    collisions = sum(has_collision(group_size) for _ in range(trials))
    return collisions / trials

if __name__ == "__main__":
    for size in [10, 20, 23, 30, 40, 50]:
        probability = estimate(size)
        print(f"group={size:2d}  collision≈{probability:6.2%}")
