# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set(map(int,input().split()))
# set1=sorted(set1)
t=int(input())
while(t>0):
    t-=1
    strings=input().split()
    if strings[0]=="pop":
        if set1:
           set1.remove(min(set1))
    elif strings[0]=="remove":
        x=int(strings[1])
        if x in set1:
           set1.remove(x)
    elif strings[0]=="discard":
        set1.discard(int(strings[1]))
print(sum(set1))