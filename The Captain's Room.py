# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
li=list(map(int,input().split()))
max_number=max(li)
freq=[0]*(max_number+1)
for x in li:
    freq[x] +=1
for val, counter in enumerate(freq):
    if 0<counter<k:
        print(val)
        break