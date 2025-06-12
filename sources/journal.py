import os
import json
from typing import List, Dict

class Journal:
    """Simple journal system for storing daily health data."""

    def __init__(self, path: str = "journal.json") -> None:
        self.path = path
        self.entries: List[Dict] = []
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self.entries = json.load(f)
            except json.JSONDecodeError:
                self.entries = []

    def _save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=2)

    def add_entry(self, entry: Dict) -> None:
        self.entries.append(entry)
        self._save()

    def all_entries(self) -> List[Dict]:
        return self.entries
