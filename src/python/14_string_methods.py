name = "NiTiN cHoUdHaRy"

# 1. len() function
print(len(name))

# 2. lower() method
print(name.lower())

# 3. upper() method
print(name.upper())

# 4. title()  method
print(name.title())

# 5. count() method
print(name.count("i"))

# 6. understanding strip methods
name = "     Nitin    "
dots = "............."
print (name + dots)
print (name.lstrip() + dots)
print (name.rstrip() + dots)
print (name.strip() + dots)

# 7. understand replace methods
name = "    Nit   in   "
print (name.replace(" ","")+dots)

string = "she is beautiful and she is good dancer"
print(string.replace("she","Nidhi"))
print(string.replace("she","Nidhi",1))

# 8. find() method
print(string.find("is"))
print(string.find("is",14))
print(string.find("is",string.find("is")+1))

# 9. understand center method
name = "Nitin"
print(name.center(11,"*"))
name  = input("Enter your name : ")
print(name.center(len(name)+8,"*"))