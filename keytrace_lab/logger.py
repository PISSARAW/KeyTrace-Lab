"""
logger.py
=========
Keyboard-event capture and safe, path-restricted log writing.

"""

from __future__ import annotations

import pathlib
from datetime import datetime, timezone
from typing import Optional

# Absolute path to the controlled log directory.
# All log output must stay inside this folder.
LAB_LOGS_DIR: pathlib.Path = (
    pathlib.Path(__file__).parent.parent / "lab_logs"
).resolve()


class KeyLogger:
    """
    Captures keyboard events and writes them to a file in lab_logs/.

    Parameters
    ----------
    log_filename:
        Name of the log file (must not contain path separators).
        The file will be created inside LAB_LOGS_DIR automatically.

    Attributes
    ----------
    event_count : int
        Number of events recorded in the current session.
    is_running : bool
        Whether the logger is currently active.
    """

    def __init__(self, log_filename: str = "session.log") -> None:
        self.log_filename = log_filename
        self.event_count: int = 0
        self.is_running: bool = False
        self._log_path: Optional[pathlib.Path] = None

    # ------------------------------------------------------------------
    # Public interface (implement these)
    # ------------------------------------------------------------------

    def start(self) -> None:
        """
        Prepare the logger for a new session.
        This method should be called before attaching the on_press and on_release callbacks to a pynput listener.
        """
        if not LAB_LOGS_DIR.exists():
            LAB_LOGS_DIR.mkdir(parents=True)
        self._log_path = (LAB_LOGS_DIR / self.log_filename).resolve()
        if not str(self._log_path).startswith(str(LAB_LOGS_DIR)):
            raise ValueError("Log filename must be inside lab_logs/")
        self.is_running = True
        self.event_count = 0

    def stop(self) -> None:
        """
        Cleanly terminate the logging session.
        After calling this method, on_press() and on_release() should do
        nothing until start() is called again.
        """
        self.is_running = False
        if self._log_path is not None:
            self._write_record("=== SESSION ENDED ===")

    def on_press(self, key: object) -> None:
        """
        pynput callback — called on every key-press event.

        Parameters
        ----------
        key:
            A pynput Key or KeyCode object.

        """
        if not self.is_running:
            return
        record = f"{self._timestamp()} PRESS {str(key)}"
        self._write_record(record)
        self.event_count += 1

    def on_release(self, key: object) -> None:
        """
        pynput callback — called on every key-release event.

        Parameters
        ----------
        key:
            A pynput Key or KeyCode object.

        """
        if not self.is_running:
            return
        record = f"{self._timestamp()} RELEASE {str(key)}"
        self._write_record(record)
        self.event_count += 1

    # ------------------------------------------------------------------
    # Private helpers (implement these)
    # ------------------------------------------------------------------

    def _write_record(self, record: str) -> None:
        """
        Append *record* (one line) to self._log_path.

        This method must raise ValueError if self._log_path is not set or
        is not inside LAB_LOGS_DIR.
        """
        if self._log_path is None or not str(self._log_path).startswith(str(LAB_LOGS_DIR)):
            raise ValueError("Log path is not set or is outside lab_logs/")
        with self._log_path.open("a", encoding="utf-8") as f:
            f.write(record + "\n")

    @staticmethod
    def _timestamp() -> str:
        """Return the current UTC time as an ISO-8601 string."""
        return datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
