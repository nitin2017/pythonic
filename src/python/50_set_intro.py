# unordered collection of unique items

s = {1,2,3,2} # curly brackets used to declare set but not in key value form
# set cannot store list , tuple or dictionary in it

print(s) # {1, 2, 3}  duplicate 2 is removed 
print(type(s)) # <class 'set'>
l = [1,1,2,2,3,3,4,4,5,5,5,6,6,7,7,8,8,9,9,]
#  remove duplicates
s2 = set(l)
print(s2)

### some methods for sets 

s.add(4)
print(s) # {1, 2, 3, 4} 4 added

s.remove(4)
print(s) # {1, 2, 3} 3 removed

## s.remove(5) #this will give KeyError as 5 doen't exist in set
s.discard(5) # this will not give any error nor it will remove 5 as it doesn't exist

s1 = s.copy()
print(s1 is s)
print(s1 == s)