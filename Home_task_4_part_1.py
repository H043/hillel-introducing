values = [1, 2, 3, 4, 5]
# print(type(values))

# values = (1, 2, 3, 4, 5)
# print(type(values))

# values = list(values)
# # print(type(values))
# values = tuple(values)
# print(type(values))
# result = []
#
# for value in values[::-1]:
#     result.append(value)
# print(result)
# print(len(values))
# new_value = values + values[::-1]
# print(new_value)
new_value = values
new_value.append(67)
print(new_value)