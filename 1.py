# print('hello')
# print("qwerty")
# my_int = 10
# print('my_int', type(my_int))
# my_float = 10.2
# my_str = "10"
# print(my_str,my_int,my_float, type(my_int), type(my_float), type(my_str))
# my_value = int(input("enter anything"))
# print(my_value*12, type(my_value))
# my_new_int = int(my_float)
# print(my_new_int, type(my_new_int))

#my_bool = 2 != 3
#my_new_bool = not my_bool
#print(my_bool, type(my_bool))
#print(my_new_bool, type(my_new_bool))

# my_int =0 #0 - always false / any number - always true
# my_bool = bool(my_int)
# print(my_bool)

# my_float =0.0000000000000000000000000000000002 #0 - always false / any number - always true
# my_bool_ = bool(my_float)
# print(my_bool_)

# my_val = 1.1231289351827653
# my_val2 = 1.123128937
# print(abs(my_val - my_val2) < 0.0001)

# my_str = "false"
# my_bool = bool(my_str) #пустая строка только false, остальное true
# print(my_bool, type(my_bool))

#
# temperature = int(input("how many degree?"))
# if temperature < 10:
#     print("STAY HOME")
# elif temperature >10:
#     print("take a beer")
# else:
#     print("Go WALK")
#
# number = 12.2
# if not number % 2:
#     print("good")
# else:
#     print("nogood")



#LESSON 3

# str_value = input("enter str ")
# new_str_value = str_value[0]+str_value[-1]
# print(new_str_value)
#
# int_value = int(input("ewh"))
# if str(int_value) [-1] == '1':
#     print("ok")
# else:
#     print("not ok")


int_value = int(input("enter value "))
revers_str = str(int_value[::-1])
revers_str_clean = str(int(revers_str))
result = len(revers_str) - len(revers_str_clean)
print(result)
