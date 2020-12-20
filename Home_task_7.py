import random
my_rand = [random.randint(0, 101) for i in range(20)]
print(my_rand)
########################################
def r_coordinates():
    return tuple(random.randint(-10, 10) for i in range(2))
triangle = {"A":r_coordinates(), "B": r_coordinates(), "C": r_coordinates()}
print(triangle)
########################################
my_str = "I AM STRING!"
def my_print(my_str):
    my_str = "***" + my_str + "***"
    return my_str
if type(my_str) == str:
    my_str = my_print(my_str)
print(my_str)
#######################################
persons = [{"name": "John", "age": 19},
           {"name": "Jimmy", "age": 25},
           {"name": "Jany", "age": 28},
           {"name": "Janet", "age": 19}]
youngest_age = min(person["age"] for person in persons)
youngest_person = [person["name"] for person in persons if person["age"] == youngest_age]
longest_name = max(len(person["name"]) for person in persons)
long_name_person = [person["name"] for person in persons if len(person["name"]) == longest_name]
print(youngest_person, long_name_person)
########################################

my_dict_1 = {'key1': 0, "key2": 2, "key3": 5, "key4": 22}
my_dict_2 = {'key1': 0, "key_2": 4, "key3": 6, "key_4": 22}
my_list_common_key = []
# A)
for key in my_dict_1.keys() and my_dict_2.keys():
    if key in my_dict_1.keys() and my_dict_2.keys():
        my_list_common_key.append(key)
print(my_list_common_key)
# B)
my_list_1dict_keys = list(set(my_dict_1).difference(set(my_dict_2)))
print(my_list_1dict_keys)
# C)
new_dict = {key: my_dict_1[key] for key in my_list_1dict_keys}
print(new_dict)
# D).1
one_time_key1 = {key: my_dict_1[key] for key in list(set(my_dict_1).difference(set(my_dict_2)))}
one_time_key2 = {key: my_dict_2[key] for key in list(set(my_dict_2).difference(set(my_dict_1)))}
new_dict_one_time = {**one_time_key1, **one_time_key2}
print(new_dict_one_time)
# D).2
common_key_dict = {key: [my_dict_1[key], my_dict_2[key]] for key in my_list_common_key}
print(common_key_dict)