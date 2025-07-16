if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nums=set(arr)
    newlist=list(nums)
    newlist.sort()
    print(newlist[-2])