fruits = ['grapes','mango','apple']
# sort
fruits.sort()
print(fruits)

fruits2 = ('grapes','mango','apple')
#fruits2.sort() ## tuples are immutable and hence this will fail
print(sorted(fruits2))

fruits3 = {'grapes','mango','apple'}
print(sorted(fruits3))

guitars = [
    {'model':'abc','price':26000},
    {'model':'xyz','price':8000},
    {'model':'pqr','price':94000},
    {'model':'yam','price':32000}
]

## Sort above list of dictionaries  based on price 

print(list(sorted(guitars, key = lambda d:d['price'] ))) # asc order
print(list(sorted(guitars, key = lambda d:d['price'],reverse =True ))) # desc order

