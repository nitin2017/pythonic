# first class functions/ closures
# then we finally learn about decorators

def square(a):
    return a**2

s =  square # u assign square to a variable , not calling square
print(s(7))
print(s.__name__)
print(s)  ## <function square at 0x000002B6919D2F28>
print(square) ## <function square at 0x000002B6919D2F28>