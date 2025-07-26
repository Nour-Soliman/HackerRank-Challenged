import numpy
n,m=map(int,input().split())
a=numpy.array([list(map(int,input().split())) for _ in range(n)])
b=numpy.array([list(map(int,input().split())) for _ in range(n)])
print(a+b)
print(a-b)
print(a*b)
print(a//b)# Avoid division by zero if possible
print(a%b)
print(a**b)