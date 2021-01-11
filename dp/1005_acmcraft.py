###### 단순 dfs -> 실패 ㅠ

import sys

input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(100000)

def get_time(building):
    #이미 계산한 적 있으면
    if dp[building] != 0:
        return dp[building]
    else:
        tmp = 0
        # 맨 처음 지어야하는 빌딩
        if building in pre.keys():
            for i in pre[building]:
                tmp = max(tmp, get_time(i))
        dp[building] = tmp + time[building]
        return dp[building]

tc = int(input())
answer = []
for i in range(tc):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    pre = {}    #건물 i 직전에 지어야 하는 건물 저장
    for j in range(N+1):
        pre[j] = []
    
    for j in range(K):
        before, after = map(int, input().split())
        pre[after].append(before)
    W = int(input())

    dp = [0]*(N+1)
    # 건물 i를 짓는데 걸리는 시간 = max(직전에 지어야 하는 건물 소요시간) + 지금건물 짓는 소요시간
    answer.append(get_time(W))

for a in answer:
    print(str(a)+'\n')