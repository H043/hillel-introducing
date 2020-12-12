# import random
# # my_rand = [random.randint(0, 101) for i in range(20)]
# # print(my_rand)
# # ########################################
#
# coor_A= tuple([random.randint(-10, 10) for i in range(2)])
# coor_B= tuple([random.randint(-10, 10) for i in range(2)])
# coor_C= tuple([random.randint(-10, 10) for i in range(2)])
# triangle = {"A":coor_A, "B": coor_B, "C": coor_C}
# print(triangle)
# ########################################
# my_str = "ENTER SOMETHING"
# def my_print(my_str):
#     my_str = "***" + my_str + "***"
#     return my_str
# if type(my_str) == str:
#     my_str = my_print(my_str)
# print(my_str)
# ########################################
my_team = [{"name": "John", "age": 19}, {"name": "Jim", "age": 25}, {"name": "Jany", "age": 28}, {"name": "Janet", "age": 19}]
my_team_age = []
my_team_name = []
asd = []
for symbol in my_team:
    my_team_age.append(symbol["age"])
    my_team_name.append(symbol["name"])
aver_age = sum(my_team_age) / len(my_team_age)
print(my_team_age,
      my_team_name,
    min(my_team_age))

print(my_team)