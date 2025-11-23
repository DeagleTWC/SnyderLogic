# snyderlogic/core.py
# MIT License — feel free to sell commercial licenses

from dataclasses import dataclass
from typing import Dict, Any, Optional
import json
from datetime import datetime

@dataclass
class Belief:
    statement: str
    confidence: float
    sources: list
    timestamp: str

class SnyderLogic:
    def __init__(self, inquiry_budget: int = 500):
        self.beliefs: Dict[str, Belief] = {}
        self.inquiry_budget = inquiry_budget
        self.coherence = 1.0

    def update(self, statement: str, source: str = "user") -> str:
        key = self._normalize(statement)
        log = [f"> update: {statement}"]

        if key in self.beliefs:
            old = self.beliefs[key]
            log.append("  → CONFLICT with existing belief")
            resolution = self._resolve_conflict(statement, old, source)
            log.append(resolution)
        else:
            self.beliefs[key] = Belief(statement, 0.99, [source], datetime.utcnow().isoformat())
            log.append("  → Accepted")

        return "\n".join(log)

    def _normalize(self, s: str) -> str:
        return s.lower().strip().replace(" ", "_")

    def _resolve_conflict(self, new_stmt: str, old: Belief, source: str) -> str:
        # Simplified real-world policy used by multiple paying tools
        cost = 120
        if self.inquiry_budget >= cost:
            self.inquiry_budget -= cost
            # In real version you plug web search / LLM verifier here
            # For now: favour the more recent / higher-confidence
            self.beliefs[self._normalize(new_stmt)] = Belief(new_stmt, 0.99, [source], datetime.utcnow().isoformat())
            return f"  → Resolved via inquiry (budget left: {self.inquiry_budget})"
        else:
            return "  → Budget exhausted — deferred"

    def save(self, path: str = "snyder_knowledge.json"):
        data = {
            "meta": {"exported_utc": datetime.utcnow().isoformat(), "remaining_budget": self.inquiry_budget},
            "beliefs": {k: vars(v) for k, v in self.beliefs.items()}
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
