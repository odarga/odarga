from numb3rs import validate

def test_one():
    assert validate("127.0.1") == False

def test_two():
    assert validate("255.2.129.0") == True

def test_three():
    assert validate("512.34.127.11") == False

def test_four():
    assert validate("124.22.3.1000") == False

def test_four():
    assert validate("cat") == False
