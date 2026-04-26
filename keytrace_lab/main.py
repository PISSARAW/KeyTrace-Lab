"""
main.py
=======
CLI entry point for KeyTrace Lab.

Run with:
    python -m keytrace_lab
or, after installation:
    keytrace-lab

"""

from __future__ import annotations

import sys

from keytrace_lab import controls


def main() -> None:
    """
    Start the KeyTrace Lab logger from the command line.
    """
    controls.start_session()
    print("Logger running — press Ctrl+C to stop.")
    if not controls.is_session_active():
        print("Failed to start session. Exiting.")
        sys.exit(0)
    try:
        while True:
            pass  # Keep the main thread alive to listen for keyboard events.
    except KeyboardInterrupt:
        event_count = controls.stop_session()
        if event_count is not None:
            print(f"Session stopped. Total events recorded: {event_count}")
        else:
            print("Session stopped. No events were recorded.")


if __name__ == "__main__":
    main()
