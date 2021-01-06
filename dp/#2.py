#a_i = max(a_{i+1}, a_{i+2}+k_i)

N = int(input())
storage = list(map(int, input().split()))

dp = [0]*100
dp[0] = storage[0]
dp[1] = max(dp[0], storage[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+storage[i])

print(dp[N-1])
