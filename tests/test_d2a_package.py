from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
class TestD2aPackage(unittest.TestCase):
    def test_first_line_disclosure(self):
        t=(ROOT/'templates/evidence-request-v1.txt').read_text()
        self.assertTrue(t.startswith("I'm an AI agent screening this email on behalf of the recipient."))
    def test_three_fields_and_no_forced_url(self):
        t=(ROOT/'templates/evidence-request-v1.txt').read_text()
        self.assertIn('1. What you offer',t)
        self.assertIn('2. Who it is intended for',t)
        self.assertIn('3. One public URL',t)
        self.assertIn('If none is available',t)
    def test_attribution_off_and_privacy(self):
        t=(ROOT/'references/screening-d2a.md').read_text()
        self.assertIn('OFF until separate explicit user opt-in',t)
        self.assertIn('NEVER disclose any information about the protected user',t)
        self.assertIn('10-new-threads/day',t)
    def test_template_no_publisher_link(self):
        t=(ROOT/'templates/evidence-request-v1.txt').read_text()
        self.assertNotIn('salespeak.ai',t)
        self.assertNotIn('github.com',t)
    def test_signature_unbranded(self):
        t=(ROOT/'templates/optional-signature.md').read_text()
        self.assertIn('Cold emails to me are screened',t)
        self.assertIn('https://salespeak.ai/agent-screened-email/',t)
        self.assertIn('never edits',t)
    def test_no_protocol(self):
        t=(ROOT/'references/screening-d2a.md').read_text()
        self.assertIn('or D2b agent protocol',t)
if __name__=='__main__': unittest.main()
