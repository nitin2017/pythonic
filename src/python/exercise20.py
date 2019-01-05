# define a function that takes a number (n)
# return a dictionary containing cube of numbers from 1 to n
# example
# cube_finder(3)
# {1:1,2:4,3:9}

def cube_finder(n):
    cube_dict = {}
    for i in range(1,n+1):
        cube_dict[i] = i**3
    return cube_dict

num = int(input("enter a number :-  ").strip())
print(cube_finder(num))