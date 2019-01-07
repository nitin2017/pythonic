# function returning function

def outer_func():
    def inner_func():
        print ("inside inner func")
    return inner_func

var = outer_func()
print(var) # <function outer_func.<locals>.inner_func at 0x0000020806720268>
print(type(var)) # <class 'function'>

var() ## inside inner func

# another example

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var2 = outer_func2("hello there")
var2() 