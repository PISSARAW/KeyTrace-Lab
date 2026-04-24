"""
Tests for keytrace_lab.consent
===============================
These tests verify the public interface of the consent module so that when
you implement the stubs the tests serve as a concrete specification.
"""

from __future__ import annotations

import importlib
import types

import pytest

import keytrace_lab.consent as consent_mod


class TestModuleConstants:
    """The consent module must expose the required constants."""

    def test_warning_banner_is_string(self):
        assert isinstance(consent_mod.WARNING_BANNER, str)

    def test_warning_banner_not_empty(self):
        assert len(consent_mod.WARNING_BANNER.strip()) > 0

    def test_consent_phrase_is_string(self):
        assert isinstance(consent_mod.CONSENT_PHRASE, str)

    def test_consent_phrase_not_empty(self):
        assert len(consent_mod.CONSENT_PHRASE.strip()) > 0


class TestDisplayWarning:
    """display_warning() must be a callable that is implemented."""

    def test_is_callable(self):
        assert callable(consent_mod.display_warning)

    def test_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement the function."""
        with pytest.raises(NotImplementedError):
            consent_mod.display_warning()


class TestRequestConsent:
    """request_consent() must return bool and honour the consent phrase."""

    def test_is_callable(self):
        assert callable(consent_mod.request_consent)

    def test_raises_not_implemented_until_filled_in(self):
        """Skeleton guard: remove this test once you implement the function."""
        with pytest.raises(NotImplementedError):
            consent_mod.request_consent()

    # ------------------------------------------------------------------ #
    # Uncomment and complete these tests when you implement request_consent
    # ------------------------------------------------------------------ #

    # def test_returns_true_on_correct_phrase(self, monkeypatch):
    #     monkeypatch.setattr("builtins.input", lambda _: consent_mod.CONSENT_PHRASE)
    #     assert consent_mod.request_consent() is True

    # def test_returns_false_on_wrong_phrase(self, monkeypatch):
    #     monkeypatch.setattr("builtins.input", lambda _: "no")
    #     assert consent_mod.request_consent() is False

    # def test_returns_false_on_empty_input(self, monkeypatch):
    #     monkeypatch.setattr("builtins.input", lambda _: "")
    #     assert consent_mod.request_consent() is False
