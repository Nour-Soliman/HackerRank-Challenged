import numpy
n=int(input())
arr=numpy.array([list(map(float,input().split(' '))) for _ in range(n)])
print(round(numpy.linalg.det(arr),2))