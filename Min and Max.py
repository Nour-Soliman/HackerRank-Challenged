import numpy
n,m=map(int,input().split(' '))
arr=numpy.array([list(map(int,input().split(' '))) for _ in range(n)])
minimum=numpy.min(arr,axis=1)
print(numpy.max(minimum))