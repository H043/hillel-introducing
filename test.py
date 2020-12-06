#
# my_list = [1, 2, 3, 4]
# for i in range(1, len(my_list), 1):
#     my_list[i-1], my_list[i] = my_list [i], my_list[i-1]
#     print(my_list)
# # print(my_list)
example_string = 'aaasssdd`'
my_random = ''.join(list(set(example_string)))
print(my_random)

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