# SecureKeyLab 🔐

A Python desktop application for learning keyboard-event handling, local logging, and basic security testing.

## Overview

SecureKeyLab is an educational project built with Python and Tkinter. It demonstrates how keyboard events can be handled within a dedicated application input field and recorded as timestamped JSON Lines (JSONL) entries.

## Features

- Desktop interface built with Tkinter
- Explicit Start and Stop controls
- Keyboard-event timestamps
- Local JSONL logging
- Event counter and log-clearing functionality
- Automated unit tests
- Security analysis and privacy documentation

## Technology Stack

- Python
- Tkinter
- JSON and JSONL
- unittest
- Git and GitHub

## Getting Started

### Requirements

- Python 3.10 or later
- Tkinter support

### Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd SecureKeyLab
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Run the application:

```bash
python app.py
```

### Run Tests

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
SecureKeyLab/
├── app.py
├── event_processor.py
├── local_logger.py
├── tests/
├── docs/
├── .gitignore
└── README.md
```

## Privacy and Security

- Keyboard events are processed only within the application's designated input field.
- The application records key names and timestamps, not the typed character values.
- Event records are stored locally.
- No remote data transmission is implemented.
- Local logs may contain sensitive behavioral information and should not be committed to version control.

Use synthetic test input only.

## Limitations

This project is an educational demonstration, not a production monitoring or forensic tool. Its current tests cover the event processor and local logger; GUI behavior and security boundaries require additional testing.

## Future Improvements

- Additional failure-handling tests
- Improved accessibility and interface feedback
- Configurable log retention
- Expanded automated testing

## Author

Vedansh Verma

## License

This project is licensed under the MIT License.
