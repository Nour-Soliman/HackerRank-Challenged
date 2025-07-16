if __name__ == '__main__':
    li=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name,score])
    scores = sorted(set([s[1] for s in li]))
    second_lowest = scores[1]
    result = sorted([s[0] for s in li if s[1] == second_lowest])
    for name in result:
        print(name)