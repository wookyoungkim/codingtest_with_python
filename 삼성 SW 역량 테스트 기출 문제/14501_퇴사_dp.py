import sys

input = sys.stdin.readline

N = int(input())
time = []
profit = []
dp = [0]*(N+1)
answer = 0
for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

for i in range(N-1, -1, -1):
    #  남은 기간보다 상담일이 긴 경우
    if time[i] + i > N:
        #해당 일의 상담은 x
        dp[i] = dp[i+1]
    else:
        #오늘 상담할 수 있는 경우 : 오늘 상담 안한 경우와 한 경우중 최대
        dp[i] = max(dp[i+1], profit[i]+dp[i+time[i]])
print(dp[0])