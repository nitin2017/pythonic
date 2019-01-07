# map
def square(a):
    return a**2

l = [1,2,3,4]
print(list(map(lambda a:a**2,l)))

## fucn as arguement

def my_map(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list

# using list comp

def my_map2(func,l):
    return [func(item) for item in l]

print(my_map(square,l))
print(my_map(lambda a:a**2,l))
print(my_map2(square,l))