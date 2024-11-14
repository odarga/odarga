from working import convert
import pytest

def test_one():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_two():
    assert convert("9:20 AM to 5:35 PM") == "09:20 to 17:35"

def test_three():
    assert convert("9 PM to 12 AM") == "21:00 to 00:00"

def test_four():
    assert convert("9:10 PM to 12:40 AM") == "21:10 to 00:40"

def test_one_error():
    with pytest.raises(ValueError):
        convert("9:60 PM to 12:40 AM")

def test_two_error():
    with pytest.raises(ValueError):
        convert("9:20 PM - 12:40 AM")

def test_three_error():
    with pytest.raises(ValueError):
        convert("9:20 PM - 17:40 AM")
