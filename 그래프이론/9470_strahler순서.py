import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    #indegree가 0인 노드에 대해서
    queue = deque()
    answer = []

    for i in range(1, M+1):
        if indegree[i] == 0:
            queue.append(i)
            strahler[i] = 1
    while queue:
        now = queue.popleft()
        answer.append(now)
        for i in graph[now]:
            #연결 간선 끊기
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    print(answer)

tc = int(input())
for i in range(tc):
    K, M, P = map(int, input().split())
    indegree = [0]*(M+1)
    strahler = [0]*(M+1)
    graph = [[] for _ in range(M+1)]

    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

    topology_sort()
