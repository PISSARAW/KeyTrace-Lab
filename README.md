# KeyTrace Lab 🔬

> **⚠️ EDUCATIONAL USE ONLY — LOCAL ENVIRONMENT ONLY**
> This tool is designed exclusively for learning about keyboard-event capture
> in the context of malware analysis and defensive security research.
> It must **never** be deployed on any machine without the explicit, informed
> consent of its owner.

---

## Purpose

KeyTrace Lab is a local-only Python skeleton for studying how keyloggers work
from a **defensive** perspective.  Understanding how malware captures input is
the first step toward detecting, blocking, and analysing it.

The project is intentionally left as a **skeleton** so that learners can
implement each component themselves, guided by the stubs and tests already in
place.

---

## Ethical & Legal Guidelines

| ✅ Allowed | ❌ Forbidden |
|---|---|
| Run on your own machine in an isolated lab VM | Run on someone else's machine |
| Study the output to learn how keyloggers behave | Capture credentials or private data |
| Use the skeleton to build your own detection rules | Distribute any resulting binary |
| Share your learning notes with the community | Use outside a controlled lab environment |

> **By starting this tool you confirm that you own or have explicit written
> permission to monitor the machine it runs on.**

---

## Project Structure

```
KeyTrace-Lab/
├── keytrace_lab/          # Main package (implement stubs here)
│   ├── __init__.py
│   ├── consent.py         # Consent prompt & ethical warning
│   ├── logger.py          # Keyboard-event capture logic
│   ├── controls.py        # Safe start / stop helpers
│   └── main.py            # CLI entry point
├── lab_logs/              # All log output stays here (never committed)
├── tests/                 # pytest test suite
│   ├── test_consent.py
│   ├── test_logger.py
│   └── test_controls.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Quickstart

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests (all skeleton tests should pass before you start coding)
pytest

# 4. Start the logger (requires explicit consent at the prompt)
python -m keytrace_lab
```

---

## Defensive Learning Goals

After completing this project you will be able to:

1. **Explain** how a keylogger hooks into OS-level keyboard events.
2. **Identify** indicators of compromise (IOCs) produced by a running keylogger.
3. **Write detection rules** (e.g. YARA, Sigma) based on observable behaviour.
4. **Implement safe guards** — consent gates, log-path restrictions, stop signals.
5. **Discuss** the legal and ethical boundaries of security research tools.

---

## Logging

All events are written exclusively to the `lab_logs/` directory.
The logger refuses to write anywhere else.
Log files are **not** committed to the repository (see `.gitignore`).

---

## Contributing

This is a personal learning project.  If you spot an issue with the skeleton
(missing stub, broken test, unclear docstring) please open an issue.
