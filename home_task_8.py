import os

domain_list = []
def open_domain_file():
    with open("domains.txt", "r") as file:
        domain_list = []
        for line in file.readlines():
            domain_list.append(line.replace(".", "").strip())
    return domain_list
print(open_domain_file())


