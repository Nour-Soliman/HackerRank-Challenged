# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set(map(int,input().split()))
m=int(input())
set2=set(map(int,input().split()))
set_res=set()
set_res=sorted(set1^set2)
print(len(set_res))
