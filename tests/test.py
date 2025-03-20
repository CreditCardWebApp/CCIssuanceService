import pytest
import random

# Luhn algorithm to validate credit card numbers
def luhn_checksum(card_number):
    digits = [int(d) for d in card_number]
    checksum = 0
    double = False

    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
        double = not double

    return checksum % 10 == 0

# Function to generate a random credit card number with valid Luhn checksum
def generate_credit_card_number(prefix="4", length=16):
    card_number = [int(d) for d in prefix]  # Start with prefix digits

    # Generate the remaining digits except the last one (check digit)
    while len(card_number) < length - 1:
        card_number.append(random.randint(0, 9))

    # Calculate Luhn check digit
    for check_digit in range(10):
        if luhn_checksum("".join(map(str, card_number)) + str(check_digit)):
            card_number.append(check_digit)
            break

    return "".join(map(str, card_number))

# Pytest test function
@pytest.mark.parametrize("prefix,length", [
    ("4", 16),    # Visa
    ("5", 16),    # Mastercard
    ("34", 15)   # American Express
])
def test_generate_credit_card_number(prefix, length):
    card_number = generate_credit_card_number(prefix, length)
    assert len(card_number) == length
    assert luhn_checksum(card_number)
    assert card_number.startswith(prefix)
    print(f"Generated valid card: {card_number}")
