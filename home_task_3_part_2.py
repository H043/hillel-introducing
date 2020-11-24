value = int(input("enter number "))
new_value = value * 2 if value < 100 else (value * -1)
print(new_value)
####################################################
value = int(input("enter number "))
new_value = 1 if value < 100 else 0
print(new_value)
####################################################
value = int(input("enter number "))
new_value = "True" if value < 100 else "False"
print(new_value)
###################################################
my_str = input("Enter text with small letters ")
print(my_str.upper())
####################################################
my_str = input("Enter text with BIG letters ")
print(my_str.lower())
####################################################
my_str = str(input("Enter text "))
new_str = my_str * 2 if len(my_str) < 5 else (my_str)
print(new_str)
####################################################
my_str = str(input("Enter text "))
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)
####################################################
my_str = str(input("Enter anything "))
for symbol in my_str:
    if symbol.isalnum():
        print(symbol)
# ####################################################
my_str = str(input("Enter anything "))
for symbol in my_str:
    if not symbol.isalnum():
        print(symbol)
# ####################################################
my_str = str(input("Enter anything "))
for symbol in my_str:
    if not symbol.isalnum() and not symbol.isspace():
        print(symbol)