# dictionary is unordered collection of items in key:value pairs

# how to create dictionary
user = {'name':'nitin','age':28}
print(user)
print(type(user))

# second way to create dictionary

user1 = dict(name = 'Nitin',age=28)
print(user1)
print(type(user1))

# how to access data from dictionary
# we access data from dictionary on the basis of key 
print(user['name'])

# which type of data can be stored in a dictionary
# numbers , string , list 

user_info = {
    'name':'Nitin',
    'age':28,
    'fav_colors':['white','black'],
    'fav_band':['Beatles','Black Sabbath']
}

print(user_info)
print(user_info['fav_band'])

# How to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'Nitin'
user_info2['age']=28
print(user_info2)