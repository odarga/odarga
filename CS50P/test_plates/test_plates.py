from plates import is_valid

def test_less_than_two_characters():
    assert is_valid("A") == False

def test_more_than_six_characters():
    assert is_valid("AAAAAAAA") == False

def test_not_starting_with_two_letters():
    assert is_valid("1AAAA") == False

def test_first_number_is_zero():
    assert is_valid("AA0") == False

def test_letters_after_numbers():
    assert is_valid("AA0AA") == False

def test_has_period():
    assert is_valid("AA.00") == False

def test_correct():
    assert is_valid("AAB10") == True

