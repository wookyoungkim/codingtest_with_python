import sys
from collections import deque

input = sys.stdin.readline

def bfs(i):
    visited[i] = 1
    cost = money[i]
    q = deque([i])
    
    while q:
        now = q.popleft()
        for next in friend[now]:
            if visited[next] == 0:
                visited[next] = 1
                cost = min(cost, money[next])
                q.append(next)
    return cost

n,m,k = map(int,input().split())
money = [0] + list(map(int,input().split()))
friend=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

visited=[0]*(n+1)
answer = 0
for i in range(1,n+1):
    if visited[i] == 0:
        answer += bfs(i)
if answer <= k:
    print(answer)
else: print('Oh no')