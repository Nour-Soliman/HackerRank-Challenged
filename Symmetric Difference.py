# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set(map(int,input().split()))
m=int(input())
set2=set(map(int,input().split()))
set_ans=sorted(set1^set2)
for x in set_ans:
    print(x)