# Enter your code here. Read input from STDIN. Print output to STDOUT
setA=set(map(int,input().split())) #A < b==> A strict subset B all elements of B is in A but A not equal B(A have more elements not in B)
n=int(input())
ans=True
while(n>0):
    n-=1
    setB=set(map(int,input().split()))
    if not(setA > setB):
        ans=False
        break
print(ans)