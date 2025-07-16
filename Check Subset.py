# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
while(t>0):
    t-=1
    counter=0
    n=int(input())
    set1=set(map(int,input().split()))
    m=int(input())
    set2=set(map(int,input().split()))
    for i in set2:
        if i in set1: 
            counter+=1
    if counter==len(set1):
        print("True")
    else:
        print("False")