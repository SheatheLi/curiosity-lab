import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from labs.hash_avalanche.avalanche import compare
from labs.bloom_filter.bloom_filter import BloomFilter
from labs.birthday_paradox.simulate import estimate
from labs.tiny_search.tfidf_search import TinySearch
from labs.consistent_hashing.consistent_hash import HashRing

class CuriosityLabTests(unittest.TestCase):
    def test_hash_avalanche_changes_many_bits(self):
        changed, ratio = compare("curiosity", "Curiosity")
        self.assertGreater(changed, 80)
        self.assertGreater(ratio, 0.30)

    def test_bloom_filter_keeps_inserted_items(self):
        bf = BloomFilter()
        for item in ["python", "redis", "docker"]:
            bf.add(item)
        self.assertTrue(all(item in bf for item in ["python", "redis", "docker"]))

    def test_birthday_paradox_near_half_for_23(self):
        probability = estimate(23, trials=5000, seed=7)
        self.assertGreater(probability, 0.45)
        self.assertLess(probability, 0.60)

    def test_tiny_search_ranks_relevant_doc(self):
        engine = TinySearch({
            "backend": "api database redis service",
            "devops": "docker deployment nginx linux",
        })
        self.assertEqual(engine.search("docker")[0][0], "devops")

    def test_hash_ring_returns_known_node(self):
        ring = HashRing(["A", "B", "C"])
        self.assertIn(ring.get("user:42"), {"A", "B", "C"})

if __name__ == "__main__":
    unittest.main()
