"""
Tests for keytrace_lab.controls
================================
These tests verify the public interface of the session-lifecycle helpers.
"""

from __future__ import annotations

import pytest

import keytrace_lab.controls as controls_mod


class TestIsSessionActive:
    """is_session_active() must be callable and return a bool."""

    def test_is_callable(self):
        assert callable(controls_mod.is_session_active)

    def test_returns_bool(self):
        result = controls_mod.is_session_active()
        assert isinstance(result, bool)

    def test_no_session_active_by_default(self):
        # Reset state in case another test left a session running.
        controls_mod._current_session["logger"] = None
        controls_mod._current_session["listener"] = None
        assert controls_mod.is_session_active() is False


class TestStartSession:
    """start_session() must be callable with the expected signature."""

    def test_is_callable(self):
        assert callable(controls_mod.start_session)

    def test_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement start_session()."""
        with pytest.raises(NotImplementedError):
            controls_mod.start_session()

    # ------------------------------------------------------------------ #
    # Uncomment and complete these tests when you implement start_session
    # ------------------------------------------------------------------ #

    # def test_returns_false_when_consent_denied(self, monkeypatch):
    #     monkeypatch.setattr("keytrace_lab.consent.request_consent", lambda: False)
    #     assert controls_mod.start_session() is False

    # def test_returns_false_when_session_already_running(self, monkeypatch):
    #     controls_mod._current_session["logger"] = object()
    #     monkeypatch.setattr("keytrace_lab.consent.request_consent", lambda: True)
    #     assert controls_mod.start_session() is False
    #     controls_mod._current_session["logger"] = None  # cleanup


class TestStopSession:
    """stop_session() must be callable with the expected signature."""

    def test_is_callable(self):
        assert callable(controls_mod.stop_session)

    def test_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement stop_session()."""
        with pytest.raises(NotImplementedError):
            controls_mod.stop_session()

    # ------------------------------------------------------------------ #
    # Uncomment and complete these tests when you implement stop_session
    # ------------------------------------------------------------------ #

    # def test_returns_none_when_no_session_running(self):
    #     controls_mod._current_session["logger"] = None
    #     controls_mod._current_session["listener"] = None
    #     assert controls_mod.stop_session() is None


class TestCurrentSessionStructure:
    """_current_session must have the expected keys."""

    def test_has_logger_key(self):
        assert "logger" in controls_mod._current_session

    def test_has_listener_key(self):
        assert "listener" in controls_mod._current_session
