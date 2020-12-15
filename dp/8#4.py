n, m = map(int, input().split())
money = []
for _ in range(n):
    x = int(input())
    money.append(x)

dp = [10001] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(money[i], m+1):
        if dp[j-money[i]] != 10001:
            dp[j] = min(dp[j], dp[j-money[i]]+1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])