
my_list = [1, 2, 3, 4]
for i in range(1, len(my_list), 1):
    my_list[i-1], my_list[i] = my_list [i], my_list[i-1]
    print(my_list)
# print(my_list)
