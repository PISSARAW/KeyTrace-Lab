"""
consent.py
==========
Displays the ethical warning and collects explicit user consent before the
logger is allowed to start.

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


def display_warning() -> bool:
    """Print the ethical warning banner and return True if consent is given."""
    print(WARNING_BANNER)
    print("To proceed, please type the following phrase exactly:")
    print(f"  {CONSENT_PHRASE}")
    if not request_consent():
        print("Consent not given. Exiting.")
        return False
    print("Consent received. Starting logger...")
    return True

def request_consent() -> bool:
    """
    Prompt the user to type CONSENT_PHRASE and return True if they do.

    Returns
    -------
    bool
        True  — user typed the consent phrase exactly.
        False — user declined or typed something else.
    """
    user_input = input("Type here: ").strip()
    return user_input == CONSENT_PHRASE
