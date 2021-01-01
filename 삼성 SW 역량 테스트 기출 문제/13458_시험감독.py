import sys

input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())
answer = N
for i in range(N):
    if students[i] - B < 0:
        continue
    if (students[i]-B)%C != 0:
        answer += (students[i]-B) // C + 1
    else:
        answer += (students[i]-B) // C

print(answer)
