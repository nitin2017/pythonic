# input -- [True,False,[1,2,3],1,2.0,3]
# output --['1','2.0',3]

def numbers(l):
    return [str(i) for i in l if type(i)== int or type(i)== float]

inp =[True,False,[1,2,3],1,2.0,3]
print(numbers(inp))