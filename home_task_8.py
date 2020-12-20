import os
import random
from random import randint
from typing import List


def open_domain_file():
    with open("domains.txt", "r") as file:
        domain_list = []
        for line in file.readlines():
            domain_list.append(line.replace(".", "").strip())
    return domain_list
#########################################
def open_family_name():
    with open("Names.txt", "r") as family_file:
        family_names = []
        for line in family_file.readlines():
            family_names.append(line.split()[1])
    return family_names
#########################################
def random_domain():
    return random.choice(open_domain_file())


def random_name():
    return random.choice(open_family_name())


def random_number():
    return random.randint(100, 1000)


def secondary_text():
    return ''.join(chr(randint(ord("a"), ord("y"))) for i in range(randint(5, 7)))


def mail_generator():
    # new_mail = ''.join(str(r_fam) + str(r_numb) + "@" + sec_name + "." + r_domain)
    print(random_name() + "." + str(random_number()) + "@" + secondary_text() + "." + str(random_domain()))
mail_generator()
