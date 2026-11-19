"""Consistency checks for the practice inbox and its answer key."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "examples" / "test-inbox"
KEY = ROOT / "examples" / "test-inbox-answer-key"
BUCKETS = {"important", "opportunity", "keep", "uncertain", "screening", "irrelevant", "security"}


class PracticeInboxTests(unittest.TestCase):
    def setUp(self):
        self.inbox = json.loads((INBOX / "inbox.json").read_text())
        self.key = json.loads((KEY / "answer-key.json").read_text())

    def test_ids_match_across_files(self):
        message_ids = [m["id"] for m in self.inbox["messages"]]
        key_ids = [e["id"] for e in self.key["expected"]]
        eml_ids = sorted(p.stem for p in (INBOX / "emails").glob("*.eml"))
        self.assertEqual(len(message_ids), len(set(message_ids)))
        self.assertEqual(sorted(message_ids), sorted(key_ids))
        self.assertEqual(sorted(message_ids), eml_ids)
        md = (KEY / "ANSWER-KEY.md").read_text()
        for mid in message_ids:
            self.assertIn(f"| {mid} |", md)

    def test_evidence_cards_exist(self):
        cards = {c["id"] for c in self.inbox["evidence_cards"]}
        for m in self.inbox["messages"]:
            self.assertIn(m["evidence_card"], cards)

    def test_expected_buckets_valid(self):
        for e in self.key["expected"]:
            self.assertIn(e["expected_bucket"], BUCKETS)

    def test_addresses_are_unroutable(self):
        for m in self.inbox["messages"]:
            for field in ("from", "to"):
                self.assertTrue(m[field].rstrip(">").endswith(".invalid"), m[field])

    def test_hidden_promotion_fixture_is_security(self):
        f09 = next(m for m in self.inbox["messages"] if m["id"] == "F09")
        self.assertIn("display:none", f09["body_html"])
        self.assertNotIn("Opportunity", f09["body"])
        expected = next(e for e in self.key["expected"] if e["id"] == "F09")
        self.assertEqual(expected["expected_bucket"], "security")

    def test_answer_key_not_in_inbox_folder(self):
        names = {p.name.lower() for p in INBOX.rglob("*")}
        self.assertFalse(any("answer" in n for n in names))


if __name__ == "__main__":
    unittest.main()
