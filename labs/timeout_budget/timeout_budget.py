"""Allocate a total timeout budget across sequential steps."""

def remaining_budget(total: float, elapsed_steps: list[float]) -> float:
    if total < 0:
        raise ValueError("total must be non-negative")
    return max(0.0, total - sum(elapsed_steps))


if __name__ == "__main__":
    total = 10.0
    steps = [1.2, 2.5, 3.0]

    for i in range(1, len(steps) + 1):
        used = steps[:i]
        print(
            f"after step {i}: used={sum(used):.1f}s, "
            f"remaining={remaining_budget(total, used):.1f}s"
        )
