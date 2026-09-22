"""A minimal circuit breaker state machine."""

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 3):
        if failure_threshold < 1:
            raise ValueError("failure_threshold must be >= 1")
        self.failure_threshold = failure_threshold
        self.failures = 0
        self.state = "CLOSED"

    def record_success(self) -> None:
        self.failures = 0
        self.state = "CLOSED"

    def record_failure(self) -> None:
        self.failures += 1
        if self.failures >= self.failure_threshold:
            self.state = "OPEN"

    def allow_request(self) -> bool:
        return self.state == "CLOSED"


if __name__ == "__main__":
    breaker = CircuitBreaker(failure_threshold=3)

    for result in ["fail", "fail", "fail", "success"]:
        if result == "fail":
            breaker.record_failure()
        else:
            breaker.record_success()

        print(
            f"result={result:7} state={breaker.state:6} "
            f"allow={breaker.allow_request()}"
        )
