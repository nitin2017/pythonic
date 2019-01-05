# in keywords and iteration on dictionaries

user_info = {
    'name':'Nitin',
    'age':28,
    'fav_colors':['white','black'],
    'fav_band':['Beatles','Black Sabbath']
}

# check if key exists in dictionary
# in keyword is used to check on keys present in dic
if 'name' in user_info:
    print('present')
else:
    print('not present')


# check if value exists in dictionary
# in below example we are checking on base of value whether it is present or not and this not work
if 'Nitin' in user_info:
    print('present')
else:
    print('not present')

if 'Nitin' in user_info.values(): # .values() will help us iterate on values present in dict
    print('present')
else:
    print('not present')

if ['Beatles','Black Sabbath'] in user_info.values():
    print('present')
else:
    print('not present')

# loops in dictionary

for i in user_info:
    print(i) # this will give all the keys present in dict

for i in user_info.values():
    print(i) # this will gve all the values present in dict

# values method
user_info_values = user_info.values()
print(type(user_info_values))
print(user_info_values)

# keys method
user_info_keys = user_info.keys()
print(type(user_info_keys))
print(user_info_keys)

for i in user_info:
    print(user_info[i])

## items method

user_items =  user_info.items()
print(type(user_items))
print(user_items)
for key,value in user_info.items():
    print(f"KEY :- {key}       VALUE :- {value}")
