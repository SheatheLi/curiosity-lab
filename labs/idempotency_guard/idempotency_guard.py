"""A tiny in-memory idempotency guard."""

class IdempotencyConflict(Exception):
    pass


class IdempotencyGuard:
    def __init__(self):
        self._seen: dict[str, str] = {}

    def accept(self, key: str, payload: str) -> str:
        if key not in self._seen:
            self._seen[key] = payload
            return "accepted"

        if self._seen[key] == payload:
            return "duplicate-same"

        raise IdempotencyConflict(
            f"key {key!r} was reused with different payload"
        )


if __name__ == "__main__":
    guard = IdempotencyGuard()

    print(guard.accept("job-42", "move:A->B"))
    print(guard.accept("job-42", "move:A->B"))

    try:
        guard.accept("job-42", "move:A->C")
    except IdempotencyConflict as exc:
        print(f"conflict: {exc}")
