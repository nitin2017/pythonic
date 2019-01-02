name = "Nitin Choudhary"
for i in range(len(name)):
    print(name[i])
print("***********************\n***********************")
# Above approach works for every programming language 
# below approach is specific to python
for i in name:
    print(i)

num = input("Enter a number:--- ").strip()
total = 0
for i in num:
    total+=int(i)
print(total)
