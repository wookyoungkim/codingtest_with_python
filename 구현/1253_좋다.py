import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

answer = 0
for i in range(len(A)):
    start, end = 0, len(A)-1
    while start < end:
        if start == i:
            start += 1
        elif end == i:
            end -= 1
        else:
            if A[start]+A[end] == A[i]:
                answer += 1
                break
            elif A[start]+A[end] < A[i]:
                start += 1
            else:
                end -= 1

print(answer)