# map function 

nums = [1,2,3,4]

def square(a):
    return a**2

print(map(square,nums)) # <map object at 0x0000023927879BA8>

squares = list(map(square,nums))
print(squares) # [1, 4, 9, 16]

# list comp

squares2 = [i**2 for i in nums]
print(squares2)

# another example for map
names = ['nitin','abhi','rishiraj','mridul']
print(map(len, names))
len_names = list(map(len,names))
print(len_names)