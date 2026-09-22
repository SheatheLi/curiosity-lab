import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from labs.heartbeat_watchdog.watchdog import is_stale
from labs.timeout_budget.timeout_budget import remaining_budget
from labs.idempotency_guard.idempotency_guard import (
    IdempotencyGuard,
    IdempotencyConflict,
)
from labs.circuit_breaker.circuit_breaker import CircuitBreaker
from labs.token_bucket.token_bucket import TokenBucket


class DailyLabTests(unittest.TestCase):
    def test_heartbeat_boundary(self):
        self.assertFalse(is_stale(97.0, 100.0, 3.0))
        self.assertTrue(is_stale(96.9, 100.0, 3.0))

    def test_timeout_budget_never_negative(self):
        self.assertEqual(remaining_budget(5.0, [2.0, 4.0]), 0.0)

    def test_idempotency_same_and_conflict(self):
        guard = IdempotencyGuard()
        self.assertEqual(guard.accept("k1", "A"), "accepted")
        self.assertEqual(guard.accept("k1", "A"), "duplicate-same")
        with self.assertRaises(IdempotencyConflict):
            guard.accept("k1", "B")

    def test_circuit_breaker_opens(self):
        cb = CircuitBreaker(3)
        cb.record_failure()
        cb.record_failure()
        self.assertTrue(cb.allow_request())
        cb.record_failure()
        self.assertFalse(cb.allow_request())

    def test_token_bucket_refill_cap(self):
        bucket = TokenBucket(2)
        self.assertTrue(bucket.allow())
        self.assertTrue(bucket.allow())
        self.assertFalse(bucket.allow())
        bucket.refill(10)
        self.assertEqual(bucket.tokens, 2)


if __name__ == "__main__":
    unittest.main()
