#  kwargs (keyword arguements)
#  **kwargs (double start operator) 

def func(**kwargs):
     print(kwargs) # this will print as a dictionary
     print(type(kwargs))

# dictionary unpacking
d = {'name':'nitin','age':28}
func(first_name='Nitin', last_name='Choudhary', age= 28)
func(**d)