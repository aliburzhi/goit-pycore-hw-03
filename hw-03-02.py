import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int):
    if not (1 <= min_value <= 1000 and 1 <= max_value <= 1000 and min_value <= quantity <= max_value):
        return []

    random_numbers_list = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(random_numbers_list)
