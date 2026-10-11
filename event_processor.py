
from datetime import datetime


def create_event_record(key_name):
    """Create a structured record for a test-area key event."""
    return {
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "key": key_name,
        "event_type": "KeyPress",
    }
