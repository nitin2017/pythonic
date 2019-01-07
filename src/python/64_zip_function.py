# zip function

user_id = ['user1','user2','user3']
names = ['nitin','mohit','rohit']
last_names = ['choudhary','agarwal','sharma']

print(list(zip(user_id,names))) 
print(list(zip(user_id,names,last_names)))

# more about zip

#l1 = [1,3,5,7]
#l2 = [2,4,6,8]

l = [(1,2),(3,4),(5,6),(7,8)]
l1,l2 = (list(zip(*l)))
print(l1)
print(l2)

new_list =[]
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)
