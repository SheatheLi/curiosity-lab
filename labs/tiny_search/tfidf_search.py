"""A minimal TF-IDF text search engine."""
from __future__ import annotations
import math
import re
from collections import Counter

TOKEN = re.compile(r"[A-Za-z0-9_]+")

def tokenize(text: str) -> list[str]:
    return TOKEN.findall(text.lower())

class TinySearch:
    def __init__(self, documents: dict[str, str]):
        self.documents = documents
        self.tokens = {name: tokenize(text) for name, text in documents.items()}
        self.doc_count = len(documents)
        self.df = Counter()
        for tokens in self.tokens.values():
            self.df.update(set(tokens))

    def _idf(self, term: str) -> float:
        return math.log((1 + self.doc_count) / (1 + self.df[term])) + 1.0

    def search(self, query: str) -> list[tuple[str, float]]:
        q = tokenize(query)
        ranked = []
        for name, tokens in self.tokens.items():
            tf = Counter(tokens)
            score = sum(tf[t] * self._idf(t) for t in q)
            if score > 0:
                ranked.append((name, score))
        return sorted(ranked, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    docs = {
        "testing": "pytest api testing regression reliability automation",
        "backend": "fastapi database api service transaction redis",
        "devops": "docker linux deployment ci cd nginx observability",
        "security": "authentication authorization jwt idor injection security",
    }
    engine = TinySearch(docs)
    for query in ["api reliability", "docker deployment", "jwt authorization"]:
        print(f"query: {query!r}")
        for name, score in engine.search(query):
            print(f"  {name:10} {score:.3f}")
        print()
