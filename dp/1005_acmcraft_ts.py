import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    Q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)
            dp[i] = time[i-1]

    while Q:
        now = Q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now]+time[i-1], dp[i])              

            if indegree[i] == 0:
                Q.append(i)
    answer.append(dp[W])

tc = int(input())
answer = []

for _ in range(tc):

    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    
    indegree = [0] * (N+1)
    graph = [[] for i in range(N+1)]
    dp = [0] * (N+1)
        
    for _ in range(K):
        before, after = map(int, input().split())
        graph[before].append(after)
        indegree[after] += 1
    W = int(input())
    topology_sort()
    
for ans in answer:
    print(ans)