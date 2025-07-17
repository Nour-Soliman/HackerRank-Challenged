# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
li=list(map(int,input().split()))
if all(x>0 for x in li) and any(str(x)==str(x)[::-1] for x in li):
    print("True")
else:
    print("False")