
import json
from pathlib import Path


class LocalLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / "events.jsonl"

    def write_event(self, record):
        """Append one event to the local log."""
        try:
            with self.log_file.open(
                "a", encoding="utf-8"
            ) as file:
                file.write(
                    json.dumps(record) + "\n"
                )
        except OSError as exc:
            raise RuntimeError(
                "Unable to write the local event log."
            ) from exc

    def clear(self):
        """Remove the existing event log."""
        try:
            self.log_file.unlink(missing_ok=True)
        except OSError as exc:
            raise RuntimeError(
                "Unable to clear the local event log."
            ) from exc
