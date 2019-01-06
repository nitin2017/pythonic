#  * operator
#  * args

def total(a,b):
    return a+b

# print(total(2,3,4,9)) this line will give error as 2 args 
# were expected we are pushing 

def all_total(*args): # using * args we can pass many arguements 
    print(args) # (1, 2, 3, 4, 5, 6)
    print(type(args)) # <class 'tuple'>

all_total(1,2,3,4,5,6)

def all_total1(*args):
    total = 0
    for num in args:
        total += num
    return total

print(all_total1(1,2,3,4,5,6,7,8,9,10))
