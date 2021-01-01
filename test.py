import random
from random import randint

#
# my_list = [1, 2, 3, 4]
# for i in range(1, len(my_list), 1):
#     my_list[i-1], my_list[i] = my_list [i], my_list[i-1]
#     print(my_list)
# # # print(my_list)
# example_string = 'aaasssdd`'
# my_random = ''.join(list(set(example_string)))
# print(my_random)

# my_list = ["3", "6", "2", 8, 1, 9]
# my_list = list(set(my_list))
# print(my_list)
# my_list = list(set(my_list))
# print(my_list)

# ip_list_1 = ["23.123.45.1", "23.123.45.107", "23.124.45.107"]
# ip_list_2 = ["23.123.45.10", "23.123.45.107", "23.124.45.17"]
#
# # ip_set_1 = set(ip_list_1)
# # ip_set_2 = set(ip_list_2)
# #
# # ip_intersect = ip_set_1.intersection(ip_set_2)
# # ip_union = ip_set_1.union(ip_set_2)
# # # ip_set_1.update(ip_set_2)
# #
# # print(ip_set_1)
# # print(ip_set_2)
# # print(ip_intersect)
# # print(ip_union)
#
#
#
#
# alphabet_ = [chr(index) for index in range(ord("A"), ord("Z"))]
# # r_text_len = (random.randint(5, 7))
# # r_sec_name = []
# # r_numb = (random.randint(100, 999))
# # r_fam = ''.join(random.choice(open_family_name()))
# # for i in alphabet_:
# #     if len(r_sec_name) != r_text_len:
# #         r_sec_name.append(random.choice(alphabet_))
# # sec_name = ''.join(r_sec_name)
# # with open("domains.txt", "r") as file:
# #     domain_list2 = []
# #     for line in file.readlines():
# #         domain_list2.append(line.replace(".", "").strip())
# # r_domain = ''.join(random.choice(domain_list2))
# print(alphabet_)
a = "ds jhf sdf sdf sadf sadgr3q s ag sad 3 d"
#
#
# def change_space_to_newline(a):
#     count_new_line = len(a) // 3
#     new_line_indexes = []
#     while len(new_line_indexes) < count_new_line:
#         index = random.randint(10, len(a) - 10)
#         if index not in new_line_indexes:
#             new_line_indexes.append(index)
#     for index in new_line_indexes:
#         a = a[:index] + "\n" + a[index + 1:]
#
# # print(change_space_to_newline(a))
# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
import random
from random import randint
import json

r_dict = {}
list_of_float = []
true_or_false = ["true", "false"]
list_keys_quantity = []
key_name = []
for i in range(random.randint(5, 20)):
    list_keys_quantity.append(i)
for i in range(0, 11):
    list_of_float.append(i / 10)
list_2_of_randoms = []
for i in list_keys_quantity:
    list_2_of_randoms.append(random.randint(-100, 100))
    list_2_of_randoms.append(random.choice(true_or_false))
    list_2_of_randoms.append(random.choice(list_of_float))
list_of_name = []
for i in list_keys_quantity:
    list_of_name.append("".join(chr(randint(ord("a"), ord("y"))) for i in range(5)))
r_dict = {x: random.choice(list_2_of_randoms) for x in list_of_name}
with open("random_dictionary", "w") as file:
    json.dump(r_dict, file)
with open("random_dictionary", "r") as file:
    r_dict_new = json.load(file)
def create_keys(min_val = 0, max_val = 10):
    keys__ = []
    for i in range(min_val, max_val):
        keys__.append(i)
    return keys__
res = create_keys()
create_keys()
print(r_dict_new)
