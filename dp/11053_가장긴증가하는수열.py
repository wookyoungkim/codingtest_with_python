import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)
            print(dp)
print(max(dp))