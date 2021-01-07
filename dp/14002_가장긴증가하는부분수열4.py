import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [1]*(N)

#LIS 알고리즘
for i in range(1, N):
    for j in range(0, i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
order = max(dp)
answer = []

for i in range(N-1, -1, -1):
    if dp[i] == order:
        answer.append(seq[i])
        order -= 1
answer.reverse()

for a in answer:
    print(a, end=' ')
