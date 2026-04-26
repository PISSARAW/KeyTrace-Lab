"""
controls.py
===========
Safe start / stop lifecycle helpers for a KeyLogger session.

"""

from __future__ import annotations

from typing import Optional

from keytrace_lab import consent as _consent
from keytrace_lab.logger import KeyLogger

# Internal state — do not access directly from outside this module.
_current_session: dict = {
    "logger": None,    # KeyLogger instance
    "listener": None,  # pynput Listener instance
}


def start_session(log_filename: str = "session.log") -> bool:
    """
    Request user consent and, if granted, start a logging session.

    Parameters
    ----------
    log_filename:
        Name of the log file to create inside lab_logs/.

    Returns
    -------
    bool
        True  — session started successfully.
        False — user declined consent or a session is already running.

    """
    if is_session_active():
        print("A session is already running. Stop it before starting a new one.")
        return False
    if not _consent.request_consent():
        return False
    logger = KeyLogger(log_filename)
    logger.start()


def stop_session() -> Optional[int]:
    """
    Stop the currently running logging session.

    Returns
    -------
    int or None
        Number of events recorded in the session, or None if no session
        was running.

    """
    if not is_session_active():
        print("No session is currently running.")
        return None
    _current_session["listener"].stop()
    event_count = _current_session["logger"].event_count
    _current_session["logger"].stop()
    _current_session["logger"] = None
    _current_session["listener"] = None
    return event_count


def is_session_active() -> bool:
    """Return True if a logging session is currently running."""
    return _current_session["logger"] is not None
