import sys
from itertools import product

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][1] = 1

for i in range(K+1):
    dp[1][i] = i

for i in range(2, N+1):
    for j in range(2, K+1):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % 1000000000

print(dp[N][K])