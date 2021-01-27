import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input())
indegree = [0]*(N+1)
roadmap = [[] for _ in range(N+1)]
time = [0]*(N+1)

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    k = 2
    for j in range(tmp[1]):
        roadmap[tmp[k]].append(i)
        indegree[i] += 1
        k += 1

def topologySort():
    queue = deque()
    result = copy.deepcopy(time)
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        for i in roadmap[now]:
            #연결 간선 끊기
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+time[i])
            if indegree[i] == 0:
                queue.append(i)

    print(max(result))

topologySort()