from seasons import get_birth_date, age_in_minute, number_to_words


def test_age_in_minute():
    assert age_in_minute(1988-11-20) == 13111

def test_number_to_words():
    assert number_to_words(243) == "Two hundred forty-three minutes"

