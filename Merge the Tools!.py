def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        substr=string[i:i+k]
        sstring=set()
        res=''
        for c in substr:
            if c not in sstring:
                sstring.add(c)
                res+=c
        print(res)