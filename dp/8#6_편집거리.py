import sys

input = sys.stdin.readline
str1 = input()
str2 = input()
n = len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = i
for i in range(1, m+1):
    dp[0][i] = i

for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            #같으면 그대로 삽입
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) #삽입, 삭제 교체 중 최소
print(dp[n][m])
