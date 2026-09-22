"""Detect stale heartbeats from a component."""

def is_stale(last_heartbeat: float, now: float, timeout: float) -> bool:
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    return (now - last_heartbeat) > timeout


if __name__ == "__main__":
    now = 100.0
    timeout = 3.0
    samples = [99.0, 97.5, 95.0]

    for last in samples:
        state = "STALE" if is_stale(last, now, timeout) else "HEALTHY"
        print(f"last={last:5.1f}s -> {state}")
