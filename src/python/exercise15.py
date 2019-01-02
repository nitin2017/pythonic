# Ask user for number of elements he wants to print in a fibonacci series and print the elements 

def fibonacci_seq(n):
    a = 0
    b = 1
    if n == 1:
        print (a)
    elif n == 2:
        print(a , b) # 1,2
    else:
        print (a,b, end = " ")
        for i in range(n-2):

            c = a + b
            a = b
            b = c
            print(b , end = " ")


input_num = int(input("Please enter number of elements of fibonacci series :- ").strip())
fibonacci_seq(input_num)