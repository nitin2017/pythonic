user ={}
name  = input("What is you name: ")
age = input("What is your age : ")
fav_color = input("Enter your fav color seperated by , : ").split(',')
fav_songs = input("Enter your fav songs seperated by , : ").split(',')

user['name'] = name
user['age'] = age
user['fav_color'] = fav_color
user['fav_songs'] = fav_songs

for key,value in user.items():
    print(f"{key} : {value}")