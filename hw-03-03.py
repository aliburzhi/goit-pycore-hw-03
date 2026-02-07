import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)

    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    if cleaned_number.startswith('38'):
        pass
    elif cleaned_number.startswith('0'):
        cleaned_number = '38' + cleaned_number
    else:
        cleaned_number = '38' + cleaned_number

    normalized_number = '+' + cleaned_number

    return normalized_number
