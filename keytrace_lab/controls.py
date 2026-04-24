"""
controls.py
===========
Safe start / stop lifecycle helpers for a KeyLogger session.

Implementation guide (fill in the TODO sections yourself)
---------------------------------------------------------
1. start_session() should call consent.request_consent(); abort if the user
   declines.
2. If consent is granted, create a KeyLogger, call logger.start(), then
   attach pynput listeners.
3. stop_session() should detach the listener and call logger.stop().
4. The module-level _current_session dict keeps track of the running logger
   and listener so that stop_session() can always reach them.
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

    TODO:
      1. Check _current_session["logger"]; return False if already running.
      2. Call _consent.request_consent(). Return False if it returns False.
      3. Instantiate KeyLogger(log_filename) and call .start().
      4. Create a pynput keyboard.Listener with on_press and on_release
         callbacks wired to the KeyLogger instance.
      5. Store both in _current_session and return True.
    """
    raise NotImplementedError("start_session() is not implemented yet")


def stop_session() -> Optional[int]:
    """
    Stop the currently running logging session.

    Returns
    -------
    int or None
        Number of events recorded in the session, or None if no session
        was running.

    TODO:
      1. Check _current_session["listener"]; return None if nothing running.
      2. Stop the pynput listener.
      3. Call logger.stop().
      4. Clear _current_session and return the event count.
    """
    raise NotImplementedError("stop_session() is not implemented yet")


def is_session_active() -> bool:
    """Return True if a logging session is currently running."""
    return _current_session["logger"] is not None
