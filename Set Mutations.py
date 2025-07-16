# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set(map(int,input().split()))
t=int(input())
while(t>0):
    t-=1
    string=input()
    name,num=string.split()
    num=int(num)
    set2=set(map(int,input().split()))
    if name=="intersection_update":
        set1.intersection_update(set2)
    elif name=="symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    elif name=="difference_update":
        set1.difference_update(set2)
    elif name=="update":
        set1.update(set2)
    
print(sum(set1))