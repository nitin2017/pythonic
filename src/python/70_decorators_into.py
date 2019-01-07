# first class functions/ closures
# then we finally learn about decorators

def square(a):
    return a**2

s =  square # u assign square to a variable , not calling square
print(s(7))
print(s.__name__)
print(s)  ## <function square at 0x000002B6919D2F28>
print(square) ## <function square at 0x000002B6919D2F28>

## decorators : enhance the functionality of another function
# @ used for decorators 
def decorator_func(any_func):
    def wrapper_func():
        print("This is awesome function")
        any_func()
    return wrapper_func
    
@decorator_func ## syntactic sugar
def func1():
    print ("This is function 1 ")

@decorator_func
def func2():
    print ("This is function 2 ")



func1()
func2()

# call function 1 or func2 and print another line " this is awesome function" without
# changing code of func1 or func2
# this can be done using decorators 
decorator_func(func1)

func1 = decorator_func(func1)
func1()
func2 = decorator_func(func2)
func2()