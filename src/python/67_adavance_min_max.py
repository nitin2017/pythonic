# advance min and max function

numbers  = [1,2,4,5,7]
print(max(numbers))  # this is simple use of max function

names = ['nitin','raghuveer','mridul']
def func(item):
    return len(item)
print(max(names,key=func))
print(min(names,key=func))

print(max(names,key = lambda item:len(item)))
print(min(names,key= lambda item:len(item)))

students = {
    'nitin':{'score':90,'age':26},
    'raghuveer':{'score':80,'age':36},
    'mridul':{'score':70,'age':19}
}

print(max(students, key = lambda item:students[item]['score'] ))


students2 = [
    {'name': 'nitin','score':90,'age':26},
    {'name': 'raghuveer' , 'score':70,'age':36},
    {'name': 'mridul' , 'score':80,'age':19}
]

print(max(students2, key = lambda item:item.get('score') ))
print(max(students2, key = lambda item:item.get('score') )['name'])

print(max(students2, key = lambda item:item.get('age') ))
print(max(students2, key = lambda item:item.get('age') )['name'])