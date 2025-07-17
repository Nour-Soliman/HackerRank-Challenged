# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
marks=[list(map(float,input().split())) for _ in range(m)]
for id_mark in zip(*marks):
    print(sum(id_mark)/m)
