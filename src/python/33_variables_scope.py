# understand variables scope

x = 5 # global variable

def func():
    global x # very rarely used 
    x = 7 #local variable
    return x

print(x)  # this will give 5 as func() is not called yet so valued assigned to variable x is still 5
print(func()) # now variables x has value 7
print(x) # now since func() has been called so we assign 7 to x 