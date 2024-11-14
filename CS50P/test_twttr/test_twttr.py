from twttr import shorten

def test_one():
    assert shorten("Onur Darga") == "nr Drg"

def test_two():
    assert shorten("Phone Number Is 5322034686") == "Phn Nmbr s 5322034686"
