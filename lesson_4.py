value = input("enter number ")
if value.isdigit():
    if int(value) !=0:
        value = int(value)
        result = 1 / value
        print(result)
    else:
        print("Division by zero")
try:
    value = int(value)
    result = 1 / value
    print(result)
except:
    print("Error")