user_info = {
    'name':'Nitin',
    'age':28,
    'fav_colors':['white','black'],
    'fav_band':['Beatles','Black Sabbath']
}

# how to add data
user_info['fav_songs'] = ['song1','song2','song3']
print(user_info)

# pop method
popped_item = user_info.pop('fav_colors') # popped_items will gold the value for the key 'fav_colors
print(popped_item)
print(user_info)

# popitem method
popped_item1 = user_info.popitem() # randomly removes one K:V pair from dict
print(popped_item1) 
print(type(popped_item1)) #<class 'tuple'>