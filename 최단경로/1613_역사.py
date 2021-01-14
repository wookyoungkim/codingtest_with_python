import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
events = [[] for _ in range(n+1)]
graph = [[INF]*(n+1) for _ in range(n+1)]
answer = []

#자기 자신에서 자기 자신으로 가는 경우
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 0

for i in range(1, n+1):
    #각각의 노드에 대해 거쳐가는 경우
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])


s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if graph[a][b] == 0:
        #a->b
        answer.append(-1)
    elif graph[b][a] == 0:
        #b->a
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a)