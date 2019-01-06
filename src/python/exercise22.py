# define a function that takes list of strings
# list containing reverse of each strings
# use list comprehension
# l = ['abc','xyz','pqr']
# reverse_string(l) --- ['cba','zyx','rqp']

def reverse_list(l):
    return [s[::-1] for s in l]

l = ['abc','xyz','pqr']
print(reverse_list(l))