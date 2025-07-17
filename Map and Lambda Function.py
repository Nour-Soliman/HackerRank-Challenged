cube = lambda x: x**3 # complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    fib=[]
    a=0
    b=1
    for _ in range(n):
        fib.append(a)
        a,b=b,a+b
    return fib