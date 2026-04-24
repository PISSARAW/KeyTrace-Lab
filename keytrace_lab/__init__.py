"""
KeyTrace Lab
============
Local-only educational keyboard-event logger for malware-analysis learning.

Modules
-------
consent   -- Ethical warning and explicit user-consent gate.
logger    -- Keyboard-event capture and safe log writing.
controls  -- Start / stop lifecycle helpers.
main      -- CLI entry point.
"""

__version__ = "0.1.0"
__all__ = ["consent", "controls", "logger", "main"]
