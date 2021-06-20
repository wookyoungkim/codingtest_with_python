import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
questions = []
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for l in range(2, N):
    # 길이가 3 이상
    for i in range(N-l):
        # 처음 문자 == 마지막 문자 && 사이가 펠린드롬
        if nums[i] == nums[i+l] and dp[i+1][i+l-1] == 1:
            dp[i][i+l] = 1


for m in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])