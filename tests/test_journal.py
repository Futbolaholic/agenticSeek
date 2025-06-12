import os
import json
import unittest

from sources.journal import Journal

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.path = 'test_journal.json'
        if os.path.exists(self.path):
            os.remove(self.path)
        self.journal = Journal(self.path)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_entry(self):
        entry = {
            'date': '2024-01-01',
            'energy': 5,
            'sleep_quality': 4,
            'supplements': ['vitamin c'],
            'mood': 'good',
            'symptoms': 'none'
        }
        self.journal.add_entry(entry)
        self.assertTrue(os.path.exists(self.path))
        with open(self.path) as f:
            data = json.load(f)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['date'], '2024-01-01')

if __name__ == '__main__':
    unittest.main()
