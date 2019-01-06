# dictionary comprehension
# square = {1:1 , 2:4 , 3:9}

square = {f"square of {num}" :num**2 for num in range(1,11) }
for k,v in square.items():
    print(f"{k} :: {v}")

##another example
# "nitin"
s = "nitin"
word_count = {char:s.count(char) for char in s}
for k,v in word_count.items():
    print(f"{k} :: {v}")


### dictionary comprehension with if else 
## d = {1:'odd',2:'even' and so on}

odd_even = {i:('even' if i%2 ==0 else 'odd') for i in range(1,11)}
for k,v in odd_even.items():
    print(f"{k} :: {v}")