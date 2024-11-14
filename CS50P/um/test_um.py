from um import count

def test_none():
    assert count("onur") == 0

def test_no_substring():
    assert count("my um name is um onur um") == 3

def test_substring():
    assert count("my um phone number um is 5322034686") == 2
