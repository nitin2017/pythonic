# function returning function (closure) practice 

# we have defined individual function to return squares or cubes 
# now we will create a function which does all things for us cubes or square

def  to_power(x): # x =3
    def calc_power(n): # n =2
        return n**x # n to power x
    return calc_power

cube  = to_power(3)
print(cube(3))  
print(cube(5))  
print(cube(6))  

square = to_power(2)
print(square(3)) 
print(square(5)) 
print(square(7)) 