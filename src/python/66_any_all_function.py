# any , all function 

num1 = [2,4,6,8,10]
num2 = [1,2,3,4,5,6]

evens1 = []
for num in num1:
    evens1.append(num%2==0)

print(all([True,True])) # --- this will return true if all values in list are True 
print(all(evens1))

print(all([num%2==0 for num in num1]))
print(all([num%2==0 for num in num2]))
print(any([num%2==0 for num in num2]))


#### more example

def my_sum(*args):
    if all([(type(i)== int or type(i)== float) for i in args]):
        tot = 0 
        for num in args:
            tot += num
        return tot
    else:
        return "Wrong Input"

print(my_sum(1,2,3,4))  ## this works will return 10
print(my_sum(1,2,3,4,8.9)) ## thsi works as well will return 18.9
print(my_sum(1,2,3,4,8.9,'nitin',['nitin'])) ## this will not work , so we have used "all" in our look to confirm all args are int or float 