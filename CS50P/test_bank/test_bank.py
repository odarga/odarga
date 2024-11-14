from bank import value

def test_hello():
    assert value("Hello, Onur Darga!") == 0

def test_h():
    assert value("How can I help you, sir?") == 20

def test_other():
    assert value("Good day to you sir!") == 100
