import re


def verify_order(message):
    if not message:
        return 0
    message = message.replace('.', '')
    message = message.replace(',', '')
    message = message.replace('\'', '')
    message = message.replace("'", '')
    print(message)
    i = 0
    max_digits = 6
    max_letters = 1

    while i < len(message) and message[i].isalpha():
        print(message[i])
        i += 1

    while i < len(message) and message[i].isdigit() and max_digits <= 0:
        i += 1
        print("digit ", message[i])
        max_digits -= 1

    while i < len(message) and message[i].isalpha() and max_letters <= 0:
        print("letter ", message[i])
        i += 1
        max_letters += 1
    print("digits", max_digits)
    print("Letters", max_letters)

    is_valid = 1 if max_digits == 0 and max_letters == 0 else 0
    return is_valid


def contains_order_number(text):
    pattern = r'\b\d{3}\.?(\d{4})\.?[A-Z]\b'
    if re.search(pattern, text):
        return 1
    else:
        return 0
