user_info = {
    'name':'Nitin',
    'age':28,
    'fav_colors':['white','black'],
    'fav_band':['Beatles','Black Sabbath']
}

more_info = {'name':'Nitin Choudhary' ,'State':'Rajasthan','hobbies':['coding','music']}

user_info.update(more_info)
for k,v in user_info.items():
    print(f"{k}     :-      {v}")