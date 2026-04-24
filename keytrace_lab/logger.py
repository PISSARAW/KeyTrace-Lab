"""
logger.py
=========
Keyboard-event capture and safe, path-restricted log writing.

Implementation guide (fill in the TODO sections yourself)
---------------------------------------------------------
1. Resolve the lab_logs/ directory relative to this file's project root.
2. On each key-press event, format a timestamped record.
3. Write records **only** to a file inside lab_logs/.  Raise ValueError if
   any caller tries to write elsewhere.
4. Expose on_press() and on_release() callbacks compatible with pynput.
5. Keep a running count of events for safe-stop decisions.
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

        TODO:
          1. Validate that LAB_LOGS_DIR exists; create it if not.
          2. Resolve the full log path and store it in self._log_path.
          3. Ensure self._log_path is inside LAB_LOGS_DIR (raise ValueError
             if not — this prevents path-traversal attacks).
          4. Set self.is_running = True and reset self.event_count = 0.
        """
        raise NotImplementedError("KeyLogger.start() is not implemented yet")

    def stop(self) -> None:
        """
        Cleanly terminate the logging session.

        TODO:
          1. Set self.is_running = False.
          2. Write a "session ended" footer to the log file.
        """
        raise NotImplementedError("KeyLogger.stop() is not implemented yet")

    def on_press(self, key: object) -> None:
        """
        pynput callback — called on every key-press event.

        Parameters
        ----------
        key:
            A pynput Key or KeyCode object.

        TODO:
          1. Guard: do nothing if self.is_running is False.
          2. Format a record: ISO-8601 timestamp + "PRESS" + str(key).
          3. Call self._write_record(record).
          4. Increment self.event_count.
        """
        raise NotImplementedError("KeyLogger.on_press() is not implemented yet")

    def on_release(self, key: object) -> None:
        """
        pynput callback — called on every key-release event.

        Parameters
        ----------
        key:
            A pynput Key or KeyCode object.

        TODO:
          1. Guard: do nothing if self.is_running is False.
          2. Format a record: ISO-8601 timestamp + "RELEASE" + str(key).
          3. Call self._write_record(record).
          4. Increment self.event_count.
        """
        raise NotImplementedError(
            "KeyLogger.on_release() is not implemented yet"
        )

    # ------------------------------------------------------------------
    # Private helpers (implement these)
    # ------------------------------------------------------------------

    def _write_record(self, record: str) -> None:
        """
        Append *record* (one line) to self._log_path.

        This method must raise ValueError if self._log_path is not set or
        is not inside LAB_LOGS_DIR.

        TODO:
          1. Check that self._log_path is not None and is relative to
             LAB_LOGS_DIR.  Raise ValueError on violation.
          2. Open self._log_path in append mode and write record + newline.
        """
        raise NotImplementedError(
            "KeyLogger._write_record() is not implemented yet"
        )

    @staticmethod
    def _timestamp() -> str:
        """Return the current UTC time as an ISO-8601 string."""
        return datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
