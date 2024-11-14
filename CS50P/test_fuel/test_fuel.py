from fuel import convert, gauge
import pytest

def test_zero_divison_error():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("5/cat")

def test_empty():
    assert gauge(0) == "E"

def test_full():
    assert gauge(99) == "F"

def test_percent():
    assert gauge(75) == "75%"
