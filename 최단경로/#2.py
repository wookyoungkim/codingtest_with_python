import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y,z])
distance = [INF]*(n+1)

pq = []
heapq.heappush(pq, [0, c])
distance[c] = 0

while pq:
    dist, now = heapq.heappop(pq)
    
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(pq, (cost, i[0]))

count = 0
max_distance = 0

for d in distance:
    if d!= INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)