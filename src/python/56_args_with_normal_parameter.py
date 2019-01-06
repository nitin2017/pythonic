#  *args with normal parameter

def multiply_nums(num , *args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,2,3))

def multiply_nums1(*args):
    multiply = 1
    
    print(args)
    for i in args:
        multiply *= i
    return multiply

l = [1,2,3,4,5,6,7,8,9,10]
print(multiply_nums1(l)) # this will not consider elements of list nstead will treat list as whole
print(multiply_nums1(*l))