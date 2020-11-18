import sys
input = sys.stdin.readline
N = int(input())
students = []

for _ in range(N):
    name, kr, en, ma = input().split()
    students.append([name, int(kr), int(en), int(ma)])

sorted_student = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(len(sorted_student)):
    print(sorted_student[i][0])
