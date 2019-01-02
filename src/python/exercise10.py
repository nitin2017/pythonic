# ask a user for Name
# Example - Nitin Choudhary
# print Count of each words
# output 
# N : 2
# I : 2
# T : 1
# c : 1
# AND SO ON 

name  = input("Enter your name :- ")
temp_var = ""
i = 0
while i<len(name):
    if name[i] not in temp_var:
        print(f"{name[i].lower()}  :  {name.lower().count(name[i].lower())}")
        temp_var += name[i].lower()
    i += 1
