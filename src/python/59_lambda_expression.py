# lambda expressions ( anonymous function)

def add(a,b):
    return a+b

add2 = lambda a,b:a+b
print(add2(2,3))

# lambda genearlly used with built in functions map , reduce ,filter

#  another example

multiply = lambda a,b:a*b 
print(multiply(3,5))

print(add) #<function add at 0x0000025A6AD62F28>
print(multiply) #<function <lambda> at 0x0000025A6B1F02F0>

##### Lambda expressions practice

def is_even(a):
    return a%2 ==0

print(is_even(3))

is_even2 = lambda a:a%2 ==0
print(is_even2(2))
print(is_even2(3)) 

def last_char(s):
    return s[-1]

last_char2 = lambda s:s[-1]

print(last_char2('abhi'))

## lambda with if,else

def func(s):
    return len(s) > 5

print(func('nitin')) 
print(func('choudhary')) 

func1 = lambda s:True if len(s) >5 else False
print(func1('choudhary'))
print(func1('nitin'))