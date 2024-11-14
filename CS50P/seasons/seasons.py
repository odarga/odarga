from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = get_birth_date()
    minutes = age_in_minute(birth_date)
    print(number_to_words(minutes))

def get_birth_date():
    try:
        year, month, day = input("Date of Birth: ").split("-")
        birth_date= date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    else:
        return birth_date


def age_in_minute(birth_date):
    today = date.today()
    delta = today - birth_date
    minutes = delta.days * 24 * 60
    return minutes


def number_to_words(minutes):
    word = p.number_to_words(minutes).replace(" and", "").capitalize()
    return f"{word} minutes"

if __name__ == "__main__":
    main()
