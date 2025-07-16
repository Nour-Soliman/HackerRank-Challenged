if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    grades = student_marks.get(query_name, [])
    if grades:
        avg=sum(grades)/3
    else:
        avg=0
    print(f"{avg:.2f}")