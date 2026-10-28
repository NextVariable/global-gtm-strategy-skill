import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    "privacy_scan", Path(__file__).resolve().parents[1] / "scripts/privacy_scan.py"
)
SCAN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCAN)


class PrivacyTests(unittest.TestCase):
    def test_private_email_stays_a_finding(self):
        self.assertEqual(
            SCAN.findings(b"person" + b"@" + b"private.invalid"), [{"rule": "email", "matches": 1}]
        )

    def test_public_noreply_and_examples_are_excluded(self):
        self.assertEqual(
            SCAN.findings(b"name@users.noreply.github.com fixture@example.invalid"), []
        )

    def test_private_path_and_credential_are_redacted(self):
        data = b"/" + b"Users/fixture " + b"ghp_" + b"a" * 35
        result = SCAN.findings(data)
        self.assertEqual({item["rule"] for item in result}, {"personal_path", "credential"})
        self.assertNotIn("fixture", str(result))


if __name__ == "__main__":
    unittest.main()
