"""
consent.py
==========
Displays the ethical warning and collects explicit user consent before the
logger is allowed to start.

Implementation guide (fill in the TODO sections yourself)
---------------------------------------------------------
1. Print the WARNING_BANNER to stdout.
2. Ask the user to type a specific confirmation phrase.
3. Return True only when the phrase matches exactly; False otherwise.
4. Never swallow the user's "no" — always honour a refusal.
"""

from __future__ import annotations

WARNING_BANNER = """
╔══════════════════════════════════════════════════════════════════╗
║              ⚠  KeyTrace Lab — EDUCATIONAL USE ONLY  ⚠          ║
║                                                                  ║
║  This tool captures keyboard events on THIS machine ONLY.        ║
║  It is designed for malware-analysis learning in an isolated     ║
║  lab environment.                                                ║
║                                                                  ║
║  ► You must own this machine OR have explicit written consent    ║
║    from its owner before proceeding.                             ║
║  ► All captured data stays in the local  lab_logs/  directory.  ║
║  ► No data is transmitted over any network.                      ║
║  ► Stop the logger at any time with  Ctrl+C  or the stop API.   ║
║                                                                  ║
║  Unauthorised use may violate computer-fraud laws.               ║
╚══════════════════════════════════════════════════════════════════╝
"""

CONSENT_PHRASE = "I understand and consent"


def display_warning() -> None:
    """Print the ethical warning banner to stdout."""
    # TODO: implement — print WARNING_BANNER
    raise NotImplementedError("display_warning() is not implemented yet")


def request_consent() -> bool:
    """
    Prompt the user to type CONSENT_PHRASE and return True if they do.

    Returns
    -------
    bool
        True  — user typed the consent phrase exactly.
        False — user declined or typed something else.
    """
    # TODO: implement
    #   1. Call display_warning()
    #   2. Print instructions: tell the user to type CONSENT_PHRASE to continue
    #   3. Read input with input()
    #   4. Return True if the stripped input == CONSENT_PHRASE, else False
    raise NotImplementedError("request_consent() is not implemented yet")
