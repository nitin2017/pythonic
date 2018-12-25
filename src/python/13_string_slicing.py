# slicing

lang = "Python"
#syntax - [start arguement: stop arguement] stop arguement -1 is used
print(lang[0:2]) # This will give Py as output
print(lang[3:6])
print (lang[-3:6])
print(lang[:])
print(lang[1:])
print(lang[:3])

# Step arguement
print("Hollywood"[0:5])   # Holly
print("Hollywood"[0:5:2]) # Hly
print("Hollywood"[0::2])
print("Hollywood"[::2])
print("Hollywood"[5::-1])
print("Hollywood"[-1::-1]) # reversed the string doowylloH
print("Hollywood"[::-1])
