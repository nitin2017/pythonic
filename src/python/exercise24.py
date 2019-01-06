# define a function
# input
# num , iterable (tuple or list) containing numbers as args
# nums =[1,2,3]
# to_power(3 ,*nums)
 
# output
# list --->[1,8,27]
# use list comprehension


def to_power(num , *args):
    if args:
        return [i**num for i in args]
    else:
        print("You didn't entered the args")

nums = [1,2,3,4,5,6,7,8,9,10]
print(to_power(3,*nums))