
import json
import tempfile
import unittest
from pathlib import Path

from local_logger import LocalLogger


class TestLocalLogger(unittest.TestCase):
    def test_write_event(self):
        with tempfile.TemporaryDirectory() as folder:
            logger = LocalLogger(folder)
            record = {
                "timestamp": "2026-10-11T10:00:00",
                "key": "a",
                "event_type": "KeyPress",
            }

            logger.write_event(record)

            lines = logger.log_file.read_text(
                encoding="utf-8"
            ).splitlines()

            self.assertEqual(len(lines), 1)
            self.assertEqual(json.loads(lines[0]), record)

    def test_clear_log(self):
        with tempfile.TemporaryDirectory() as folder:
            logger = LocalLogger(folder)
            logger.write_event({"key": "a"})

            logger.clear()

            self.assertFalse(logger.log_file.exists())


if __name__ == "__main__":
    unittest.main()
