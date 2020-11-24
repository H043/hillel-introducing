value = input("ENTER NUMBER: ")
value = int(value)
if value % 5 == 0:
    print(value * 2)
else:
    print(0)

######################################

value = input("Enter number of the month from 1 to 12 ")
value = int(value)
#ограничение диапозона ввода чисел
if 0 > value or value > 12:
    print("Enter number from 1 to 12 and try again")
if value == 2:
    print("This month has 28 days")
if value == 1 or value == 3 or value == 5 or value == 7 or value == 8 or value == 10 or value == 12:
    print("This month has 31 days")
if value == 4 or value == 6 or value == 9 or value == 11:
    print("This month has 30 days")

######################################

# value = input("enter name of the month ")
# #Исключение заглавных букв в введенном тексте
# value_ = value.lower()
# if value_ == "february":
#     print("This month has 28 days")
# if value_ == "january" or value_ == "march" or value_ == "may" or value_ == "july" or value_ == "august" or value_ == "october" or value_ == "december":
#     print("This month has 31 days")
# if value_ == "april" or value_ == "june" or value_ == "september" or value_ == "november":
#     print("This month has 30 days")

