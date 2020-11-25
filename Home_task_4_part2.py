my_list = [10, 100, 200, 300, 40, 50, 199]
for symbol in my_list:
    if symbol > 100:
        print(symbol)
#########################################

my_list = [10, 100, 200, 300, 40, 50, 199]
my_results = []
for symbol in my_list:
    if symbol > 100:
        my_results.append(symbol)
print(my_results)
#########################################

my_list_1 = [2]
my_list_2 = [1,2,3]
res = len(my_list_1)
res_2 = len(my_list_2)
if res < 2:
    my_list_1.append (0)
print(my_list_1)
if res_2 >+ 2:
    my_list_2.append(my_list_2[-1]+my_list_2[-2])
print(my_list_2)
# #########################################

value = float(input("enter float "))
try:
        value = value ** -1
        print(value,type(value))
except:
        ZeroDivisionError
        print("No good number, try again")

# #########################################
my_list = [10, 20, 30, 40]
my_indexes = [0, 1, 2, 3]
new_list = []
for index in my_indexes:
    print(my_list[index])

# #########################################
my_list_1 = [1, 2, 3]
my_list_2 = [10, 20, 30]
my_indexes = [0, 1, 2]
for index in my_indexes:
    print(my_list_1[index], my_list_2[index])

# # #########################################
my_string = "0123456789"
for symb_1 in my_string:
    for symb_2 in my_string:
        value = int(symb_1 + symb_2)
        print(value, type (value))


#type добавляю для себя как для проверки