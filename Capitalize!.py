# Complete the solve function below.
def solve(s):
    flag=True
    res=""
    for i in s:
        if flag and i.isalpha():
            res+=i.upper()
            flag=False
        else:
            res+=i
        flag=(i==" ")
    return res