# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
se1=set(map(int,input().split()))
m=int(input())
se2=set(map(int,input().split()))
se=set()
se=se1 - se2
print(len(se))