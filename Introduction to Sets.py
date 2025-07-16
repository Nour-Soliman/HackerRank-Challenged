def average(array):
    se=set(array)
    x=float(sum(se)/len(se))
    return "{:.3f}".format(x) 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)