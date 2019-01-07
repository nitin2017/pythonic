## decorators : enhance the functionality of another function
# @ used for decorators 

from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        """This is wrapper function """
        print("This is awesome function")
        return any_func(*args,**kwargs)
    return wrapper_func
    
@decorator_func ## syntactic sugar
def func(a):
    print (f"This is function with arguement {a}")

# func(7) --- this will give eror : wrapper_func() takes 0 positional arguments but 1 was given
# so we add *args or **kwargs in wrapper func

func(7) # this will work

# another example

@decorator_func
def add(a,b):
    """This is add function """
    return a+b

print(add(2,3))  # This will give None 

print(add.__doc__) ## This is wrapper function
print(add.__name__) ## wrapper_func
# for this we import functools import wrap

############################### Decorators practice #######################

# define a decorators print_function_data

from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"You are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper

@print_function_data
def add(a,b):
    """this function take two numbers as arguement and return their sum"""
    return a+b

print(add(12,13))