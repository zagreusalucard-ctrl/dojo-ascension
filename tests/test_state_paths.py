import os
import tempfile
import unittest
from pathlib import Path

import dojo_classroom


class StatePathTests(unittest.TestCase):
    def test_state_paths_follow_environment_overrides(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            custom_dir = Path(tmpdir) / "alice-dojo"
            save_path = custom_dir / "player-save.json"
            journal_path = custom_dir / "player-journal.json"

            os.environ["DOJO_DATA_DIR"] = str(custom_dir)
            os.environ["DOJO_SAVE_FILE"] = str(save_path)
            os.environ["DOJO_JOURNAL_FILE"] = str(journal_path)

            self.addCleanup(os.environ.pop, "DOJO_DATA_DIR", None)
            self.addCleanup(os.environ.pop, "DOJO_SAVE_FILE", None)
            self.addCleanup(os.environ.pop, "DOJO_JOURNAL_FILE", None)

            resolved_save, resolved_journal = dojo_classroom.get_state_paths()

            self.assertEqual(resolved_save, save_path)
            self.assertEqual(resolved_journal, journal_path)


if __name__ == "__main__":
    unittest.main()
