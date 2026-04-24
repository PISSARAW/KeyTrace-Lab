"""
main.py
=======
CLI entry point for KeyTrace Lab.

Run with:
    python -m keytrace_lab
or, after installation:
    keytrace-lab

Implementation guide (fill in the TODO sections yourself)
---------------------------------------------------------
1. Call controls.start_session().  Exit gracefully if the user declines.
2. Print a status message with the log file path.
3. Block until the user presses Ctrl+C (KeyboardInterrupt).
4. On interrupt, call controls.stop_session() and print a summary.
"""

from __future__ import annotations

import sys

from keytrace_lab import controls


def main() -> None:
    """
    Start the KeyTrace Lab logger from the command line.

    TODO:
      1. Call controls.start_session().
         - If it returns False, print a message and call sys.exit(0).
      2. Print "Logger running — press Ctrl+C to stop."
      3. Wrap a while-True / time.sleep() loop in a try/except
         KeyboardInterrupt block.
      4. In the except block, call controls.stop_session() and print the
         event count returned.
    """
    raise NotImplementedError("main() is not implemented yet")


if __name__ == "__main__":
    main()
