# TAKE TWO COMMA SEPERATED INPUTS FROM USER 
# 1.) User's Name
# 2.) single character
# output required
# 1.) user's name length
# 2.) count the coourenece of charater in user's name

user_name , character = input("Please enter comma sepearted your name and character : ").split(",")
print(f"Length of user name is {len(user_name.strip())}")
print(f"Count of occurence of character {character.strip().lower()} in user name : {user_name.lower().strip()} is {user_name.strip().lower().count(character.strip().lower())}")

