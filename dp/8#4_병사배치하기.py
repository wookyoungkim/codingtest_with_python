import sys

input = sys.stdin.readline

N = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()

#dp[i] : array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
dp = [1]*(N+1)

#LIS 알고리즘
for i in range(1, N):
    for j in range(0, i):
        print(dp)
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))