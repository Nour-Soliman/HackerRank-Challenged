def swap_case(s):
    res=""
    for i in s:
        if i.islower():
            res+=i.upper()
        else:
            res+=i.lower()
    return res
# s=input()
# print(swap_case(s))
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)