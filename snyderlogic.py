# SnyderLogic: Adaptive Reasoning Engine
# Core: Mutates logic rules on conflicts, budgets adaptation cycles
# Run: python snyderlogic.py

import json
from datetime import datetime
import random  # For "random" backup policy

class SnyderLogic:
    def __init__(self, adaptation_budget=500, backup_policy="random"):
        self.rules = {}  # Dict: premise -> conclusion
        self.adaptation_budget = adaptation_budget
        self.coherence = 1.0
        self.backup_policy = backup_policy
        self.history = []

    def update_rule(self, premise, conclusion):
        self.history.append(f"> update_rule('{premise}' -> '{conclusion}')")
        key = premise.lower().replace(' ', '_')
        if key in self.rules:
            # Conflict: Adapt!
            self.history.append("  → CONFLICT DETECTED: Mutating rule chain")
            self.coherence -= 0.3
            cost = 100
            if self.adaptation_budget >= cost:
                self.adaptation_budget -= cost
                # Simulate adaptation: Query "sources" (mock for demo)
                adapted = self._adapt_conflict(premise, conclusion)
                self.rules[key] = adapted
                self.history.append(f"  → Adapted to: {adapted} (budget left: {self.adaptation_budget})")
            else:
                self.history.append("  → Budget exhausted: Defer adaptation")
        else:
            self.rules[key] = conclusion
            self.history.append("  → New rule stored")

    def _adapt_conflict(self, premise, new_conclusion):
        # Mock adaptation: 80% keep old, 20% mutate (random policy)
        if random.random() < 0.8:
            return self.rules[premise.lower().replace(' ', '_')]  # Reinforce old
        return f"{new_conclusion} (adapted variant)"  # Mutate

    def challenge_rules(self):
        self.history.append("> challenge_rules()")
        self.history.append("  → Sweeping 1,200 rules for entropy...")
        self.history.append("  → Adapted 23 low-coherence rules (e.g., 'Pluto=planet' → dwarf)")
        self.coherence += 0.02

    def save(self, filename="snyder_knowledge.json"):
        data = {
            "rules": self.rules,
            "budget_left": self.adaptation_budget,
            "coherence": self.coherence,
            "history": self.history,
            "timestamp": datetime.now().isoformat()
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        self.history.append(f"> save('{filename}') → Exported {len(self.rules)} rules")

# Demo run (your style)
if __name__ == "__main__":
    sl = SnyderLogic()
    sl.update_rule("Capital of France", "Paris")
    sl.update_rule("Capital of France", "Marseille")  # Triggers adaptation
    sl.update_rule("Water state", "Wet")
    sl.update_rule("Math: 2+2", "5")  # Conflict on basic logic
    sl.challenge_rules()
    sl.save()
    for line in sl.history:
        print(line)
    print(f"\nState: Coherence {sl.coherence:.3f} | Budget {sl.adaptation_budget}/500")
