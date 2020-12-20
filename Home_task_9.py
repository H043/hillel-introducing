import random
from random import randint


def generate_string(min_limit=100, max_limit=1000):
    str_len = random.randint(min_limit, max_limit)
    r_list = [chr(random.randint(ord("a"), ord("z"))) for _ in range(str_len)]
    return ''.join(r_list)


def letter_to_space(str_to_transform):
    count_space = len(str_to_transform) // 5
    space_index = []
    while len(space_index) < count_space:
        index = random.randint(5, len(str_to_transform) - 5)
        if index not in space_index:
            space_index.append(index)
    for index in space_index:
        str_to_transform = str_to_transform[:index] + " " + str_to_transform[index + 1:]
    return str_to_transform


def change_first_symbol(word):
    return word.capitalize()


def change_last_symbol(word):
    punctuation = ".,!?\n"
    word = word[:-1] + random.choice(punctuation) if len(word) > 3 else word
    return word


def change_word_to_number(word):
    if len(word) <= 3:
        number_list = [str(random.randint(0, 9)) for _ in range(len(word))]
        word = "".join(number_list)
    return word


def random_word_transformation(word):
    state = random.randint(1, 6)
    if state == 1:
        word = change_first_symbol(word)
    if state == 2:
        word = change_last_symbol(word)
    if state == 3:
        word = change_word_to_number(word)
    return word


def transform_by_words(str_to_transform):
    words = str_to_transform.split()
    new_words = []
    for word in words:
        new_word = random_word_transformation(word)
        new_words.append(new_word)
    return " ".join(new_words)


res = generate_string()
res = letter_to_space(res)
res = transform_by_words(res)
print(res)
