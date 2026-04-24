"""
Tests for keytrace_lab.logger
==============================
These tests verify the public interface of the KeyLogger class and the
path-restriction invariants that protect against log-path traversal.
"""

from __future__ import annotations

import pathlib

import pytest

from keytrace_lab.logger import KeyLogger, LAB_LOGS_DIR


class TestLabLogsDir:
    """LAB_LOGS_DIR must be an absolute path pointing to lab_logs/."""

    def test_is_pathlib_path(self):
        assert isinstance(LAB_LOGS_DIR, pathlib.Path)

    def test_is_absolute(self):
        assert LAB_LOGS_DIR.is_absolute()

    def test_directory_name_is_lab_logs(self):
        assert LAB_LOGS_DIR.name == "lab_logs"


class TestKeyLoggerInterface:
    """KeyLogger must expose the expected public interface."""

    def test_instantiation_with_defaults(self):
        kl = KeyLogger()
        assert kl.log_filename == "session.log"

    def test_instantiation_with_custom_filename(self):
        kl = KeyLogger("test_run.log")
        assert kl.log_filename == "test_run.log"

    def test_initial_event_count_is_zero(self):
        kl = KeyLogger()
        assert kl.event_count == 0

    def test_initial_is_running_is_false(self):
        kl = KeyLogger()
        assert kl.is_running is False

    def test_start_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement start()."""
        kl = KeyLogger()
        with pytest.raises(NotImplementedError):
            kl.start()

    def test_stop_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement stop()."""
        kl = KeyLogger()
        with pytest.raises(NotImplementedError):
            kl.stop()

    def test_on_press_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement on_press()."""
        kl = KeyLogger()
        with pytest.raises(NotImplementedError):
            kl.on_press(None)

    def test_on_release_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement on_release()."""
        kl = KeyLogger()
        with pytest.raises(NotImplementedError):
            kl.on_release(None)


class TestKeyLoggerTimestamp:
    """_timestamp() must return a non-empty ISO-8601 UTC string."""

    def test_returns_string(self):
        ts = KeyLogger._timestamp()
        assert isinstance(ts, str)

    def test_contains_date_separator(self):
        ts = KeyLogger._timestamp()
        assert "T" in ts  # ISO-8601 datetime separator

    def test_contains_utc_offset(self):
        ts = KeyLogger._timestamp()
        # isoformat with timezone produces "+00:00" or "Z"
        assert "+" in ts or ts.endswith("Z")


    # ------------------------------------------------------------------ #
    # Uncomment and complete these tests when you implement the class
    # ------------------------------------------------------------------ #

    # def test_start_sets_is_running(self, tmp_path, monkeypatch):
    #     monkeypatch.setattr("keytrace_lab.logger.LAB_LOGS_DIR", tmp_path)
    #     kl = KeyLogger("run.log")
    #     kl.start()
    #     assert kl.is_running is True

    # def test_start_resets_event_count(self, tmp_path, monkeypatch):
    #     monkeypatch.setattr("keytrace_lab.logger.LAB_LOGS_DIR", tmp_path)
    #     kl = KeyLogger("run.log")
    #     kl.event_count = 99
    #     kl.start()
    #     assert kl.event_count == 0

    # def test_write_record_path_traversal_raises(self, tmp_path, monkeypatch):
    #     monkeypatch.setattr("keytrace_lab.logger.LAB_LOGS_DIR", tmp_path)
    #     kl = KeyLogger("run.log")
    #     kl.start()
    #     kl._log_path = tmp_path.parent / "evil.log"  # outside lab_logs
    #     with pytest.raises(ValueError):
    #         kl._write_record("bad record")
