#커리큘럼

import sys
from collections import deque
import copy

input = sys.stdin.readline

def topology_sort():
    #indegree가 0인 노드에 대해서
    queue = deque()
    result = copy.deepcopy(time)

    for i in range(1, n+1):
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
        
    for i in range(1, n+1):
        print(result[i])
        
n = int(input())
indegree = [0]*(n+1)
time = [0]*(n+1)
roadmap = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    for j in tmp[1:-1]:
        roadmap[j].append(i)
        indegree[i] += 1
topology_sort()