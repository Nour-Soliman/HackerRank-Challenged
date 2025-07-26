import numpy
n,m,p=map(int,input().split(' '))
arrn=numpy.array([list(map(int,input().split(' '))) for _ in range(n)])
arrm=numpy.array([list(map(int,input().split(' '))) for _ in range(m)])
print(numpy.concatenate((arrn,arrm),axis=0))