import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a=numpy.array(arr,float)
    return a[::-1]
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)