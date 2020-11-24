#Для упрощения кода примем, что Гендальф это Gen_, средиземье будет ML

value = input("ML is in danger? ")


hobbit = "Go and find proper Hobbit!"





good_ = "GOOD!"
call_ = "Call Eagles!"
resur_ = "Get resuracting"
if value == "yes":
    value_1 = input("somebody can solve it? ")
elif value == "no":
    print(good_)
    value_7 = input("Are you in danger? ")
    if value_7 == "yes":
        value_8 = input("THe swords can help you? ")
    elif value_7 == "no":
        print(good_)
    if value_8 == "yes":
        print(good_)
    elif value_8 == "no":
        value_6 = input("Magic can help you? ")
        while value_6 == "yes":
            print(resur_)
            value_4 = input("Problem solved? ")
            if "yes" == value_4:
                value_5 = input("Are u died? ")
            elif value_4 == "no":
                print(call_)
print(good_)
if value_1 == "yes":
    print(good_)
elif value_1 == "no":
    value_2 = input("What about hobbits? ")
if value_2 == "yes":
    print(hobbit)
    value_4 = input("Problem solved? ")
elif value_2 == "no":
    value_6 = input("Magic can help you? ")
if value_6 == "yes":
    value_4 = input("Problem solved? ")
elif value_6 == "no":
    print(call_)
if value_4 == "yes":
    value_5 = input("Are u died? ")
elif value_4 == "no":
    print(good)
while value_5 == "yes":
    print(resur_)
    value_4 = input("Problem solved? ")
    if "yes" == value_4:
        value_5 = input("Are u died? ")
    elif value_4 == "no":
        print(call_)
print(good_)





# if value_6 == "yes":
#     value_4 = input("Problem solved? ")
# else:
#     print(call_)
# if value_4 == "yes":
#
# elif value_4 == "no":
#     print(call_)
# if value_5 == "yes":
#     print(resur_)
#     value_4 = input("Problem solved? ")
# elif value_5 == "no":
#     print(good_)
