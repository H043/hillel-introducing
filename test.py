import random
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
# ip_set_1 = set(ip_list_1)
# ip_set_2 = set(ip_list_2)
#
# ip_intersect = ip_set_1.intersection(ip_set_2)
# ip_union = ip_set_1.union(ip_set_2)
# # ip_set_1.update(ip_set_2)
#
# print(ip_set_1)
# print(ip_set_2)
# print(ip_intersect)
# print(ip_union)




alphabet_ = [chr(index) for index in range(ord("A"), ord("Z"))]
# r_text_len = (random.randint(5, 7))
# r_sec_name = []
# r_numb = (random.randint(100, 999))
# r_fam = ''.join(random.choice(open_family_name()))
# for i in alphabet_:
#     if len(r_sec_name) != r_text_len:
#         r_sec_name.append(random.choice(alphabet_))
# sec_name = ''.join(r_sec_name)
# with open("domains.txt", "r") as file:
#     domain_list2 = []
#     for line in file.readlines():
#         domain_list2.append(line.replace(".", "").strip())
# r_domain = ''.join(random.choice(domain_list2))
print(alphabet_)