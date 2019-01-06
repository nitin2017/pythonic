# in keyword in sets and for loop

s = {'a','b','c','d'}

# in keyword to check if a item is prresent in list or not
if 'a' in s:
    print('present')
else:
    print('not present')

# for loop on sets 

for item in s:
    print(item)

# set maths

s1 = {1,2,3,4}
s2 = {3,4,5,6}

#union
union_set = s1 | s2
print(union_set)

#intersection
intersection_set = s1 & s2
print(intersection_set)
