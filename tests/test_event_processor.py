
import unittest
from datetime import datetime

from event_processor import create_event_record


class TestEventProcessor(unittest.TestCase):
    def test_record_contains_expected_fields(self):
        record = create_event_record("Return")

        self.assertEqual(record["key"], "Return")
        self.assertEqual(
            record["event_type"], "KeyPress"
        )
        self.assertIn("timestamp", record)

    def test_timestamp_is_valid(self):
        record = create_event_record("a")

        parsed = datetime.fromisoformat(
            record["timestamp"]
        )
        self.assertIsInstance(parsed, datetime)


if __name__ == "__main__":
    unittest.main()
