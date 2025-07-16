# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
li=list(map(int,input().split()))
set1=set(map(int,input().split()))
set2=set(map(int,input().split()))
res=0
for i in li:
    if i in set1:
        res+=1
    elif i in set2:
        res-=1   
print(res)