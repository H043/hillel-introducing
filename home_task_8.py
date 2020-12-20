import os
import random
domain_list = []
def open_domain_file():
    with open("domains.txt", "r") as file:
        domain_list = []
        for line in file.readlines():
            domain_list.append(line.replace(".", "").strip())
    return domain_list
# print(open_domain_file())
#########################################

with open("Names.txt", "r") as file:
    family_name = []
    for line in file.readlines():
        family_name.append(line.split()[1])
# print(family_name)
#########################################

def mail_generator():
   new_mail = ''.join(str(r_fam) + str(r_numb) + "@" + sec_name + "." + r_domain)
   return new_mail
alphabet_ = [chr(index) for index in range(ord("A"), ord("Z")+1)]
r_text_len = (random.randint(5, 7))
r_sec_name = []
r_numb = (random.randint(0, 999))
r_fam = ''.join(random.choice(family_name))
for i in alphabet_:
    if len(r_sec_name) != r_text_len:
        r_sec_name.append(random.choice(alphabet_))
sec_name = ''.join(r_sec_name)
with open("domains.txt", "r") as file:
    domain_list2 = []
    for line in file.readlines():
        domain_list2.append(line.replace(".", "").strip())
r_domain = ''.join(random.choice(domain_list2))
print(mail_generator())