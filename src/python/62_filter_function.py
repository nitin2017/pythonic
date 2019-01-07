# filter function

def is_even(a):
    return a%2 ==0

nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(is_even,nums))
print(evens)

odds = tuple(filter(lambda a:a%2 !=0, nums))
print(odds)

# list comp

new_evens = [i for i in nums if i%2 ==0]
print(new_evens)

new_odds = [i for i in nums if i%2 !=0]
print(new_odds)