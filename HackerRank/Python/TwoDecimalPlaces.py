# https://www.hackerrank.com/challenges/finding-the-percentage/problem

def avg(grades):
    return sum(grades) / len(grades)
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    grade = avg(student_marks[query_name])
    print(f"{grade:.2f}")