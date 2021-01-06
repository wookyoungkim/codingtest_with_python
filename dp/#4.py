#a_i : i원을 만드는데 필요한 화폐 개수, k: 화폐의 단위
#a_i = min(a_i, a_{i-k}+1)

n, m = map(int, input().split())
money = []
for _ in range(n):
    x = int(input())
    money.append(x)

dp = [10001] * (m+1)
dp[0] = 0

#각 화폐 단위 별로
for i in range(n):
    #j원 만들 수 있는지 검사
    for j in range(money[i], m+1):
        #j원 - (화폐단위) 를 만들 수 있으면
        if dp[j-money[i]] != 10001:
            dp[j] = min(dp[j], dp[j-money[i]]+1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])