# values = [1, 2, 3, 4, 5]
# values = tuple(values)


# values = (1, 2, 3, 4, 5)
# print(type(values))

# values = list(values)
# # print(type(values))

# print(type(values))
# result = []
#print(type(values))
# for value in values[::-1]:
#     result.append(value)
# print (result)
# print(len(values))
# new_value = values + values[::-1]
# # print(new_value)
# new_value = values.copy()
# new_value.append(78)
# # print(values)
# values = 0
# values = [values] * 6
# # value = 1
# # print(values)
# my_list = [0]
# values = [my_list.copy()] * 3
# my_list.append(1)
# print(values)

my_list = ["a", "b", "c", "d", "e", "f"]
my_str = "".join(my_list[::2])
print(my_str)