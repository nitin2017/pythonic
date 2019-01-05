# fromkeys method - used to create dictionary

d = {'name':'unknown','age':'unknown'}
# so basically we want to create a dict with different keys but same default value we can do this using 
# fromkeys method

d1 = dict.fromkeys(['name','age','height'],'unknown')
print(d1)

d2 = dict.fromkeys(range(1,11),'unknown')
print(d2)

d3 = dict.fromkeys(range(1,11),['unknown','unknown'])
print(d3)

# get method (useful)

d = {'name':'unknown','age':'unknown'}
print(d['name']) #  This will fetch the value for key key 'name' from dict
#print(d['names']) # this will fail and will give keyError since 'names' key doesn't exist in dict d
# In order to handle this keyError we have get method

print(d.get('name')) # This will give unknown 
print(d.get('names')) # this will not give keyError instead will give None as output

# if None the False else True : this is how below loop will be evaluated 
if d.get('name'):
    print('present')
else:
    print('not present')

# copy method 

d = {
    'name' : 'Nitin',
    'age' : 28
}

# Now we can create copy using below line as both dic will be same 
d1 = d
print(d1.popitem()) #('age', 28) we removed item from d1 but it also got removed from d since d1 is not copy of d
print(d) # {'name': 'Nitin'}

d = {
    'name' : 'Nitin',
    'age' : 28
}

d1 = d.copy()
print(d1.popitem())
print(d) # {'name': 'Nitin', 'age': 28}
print(d1)

#### more about get method 
user = {
    'name':'Nitin',
    'age':28
}

print(user.get('name'))
print(user.get('names')) # This will return None as 'names' is not present in dict
# we can override None 
print(user.get('names' , 'not found !'))

#two same keys in dictionary
user = {
    'name':'Nitin',
    'age':28,
    'age':27
}
## Second age key will override the first one 
print(user)