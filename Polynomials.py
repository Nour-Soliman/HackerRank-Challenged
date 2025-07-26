import numpy
numbers=list(map(float , input().split(' ')))
x=float(input())
print(numpy.polyval(numbers,x))