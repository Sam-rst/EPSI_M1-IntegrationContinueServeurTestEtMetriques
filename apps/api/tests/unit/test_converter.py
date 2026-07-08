"""Tests UNITAIRES : on teste la fonction pure `convert`, sans HTTP."""

import pytest

from app.converter import UnknownCurrencyError, convert


def test_convert_same_currency():
    assert convert(10, "EUR", "EUR") == 10.0


def test_convert_eur_to_usd():
    assert convert(10, "EUR", "USD") == 10.8


def test_convert_is_case_insensitive():
    assert convert(10, "eur", "usd") == 10.8


def test_convert_is_reversible():
    usd = convert(100, "EUR", "USD")
    back = convert(usd, "USD", "EUR")
    assert back == pytest.approx(100, abs=0.5)


def test_unknown_currency_raises():
    with pytest.raises(UnknownCurrencyError):
        convert(10, "EUR", "XXX")


def test_negative_amount_raises():
    with pytest.raises(ValueError):
        convert(-5, "EUR", "USD")
