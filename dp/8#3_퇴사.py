import sys

N = int(input())
days, profit = [], []
for _ in range(N):
    d, p = map(int, input().split())
    days.append(d)
    profit.append(p)

#dp[i] : i일부터 벌 수 있는 최대
#P[i] = max(money[i]+P[i+days[i]], P[i+1])
dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    #남은 기간보다 소요일이 더 길 경우
    if i+days[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(profit[i]+dp[i+days[i]], dp[i+1])
print(dp[0])