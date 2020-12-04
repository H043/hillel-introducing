from random inport randint, shuffle
DEBUG_MODE = False

def create_random_list(limit_value, limit_number):
    """Create list with random values"""
    result = [randint(1, limit_value) for _ in range(randint(1, limit_number))]
    return  result