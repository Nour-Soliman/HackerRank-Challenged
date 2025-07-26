import numpy
numpy.set_printoptions(legacy='1.13')
li=list(map(float,input().split()))
arr=numpy.array(li)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))