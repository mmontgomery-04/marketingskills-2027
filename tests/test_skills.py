import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import validate_skills  # noqa: E402


class TestSkills(unittest.TestCase):
    def test_repo_is_valid(self):
        names, errors = validate_skills.validate()
        self.assertGreater(len(names), 0)
        self.assertEqual(errors, [], "\n".join(errors))

    def test_foundation_skill_exists(self):
        names, _ = validate_skills.validate()
        self.assertIn("marketing-context", names)


if __name__ == "__main__":
    unittest.main()
