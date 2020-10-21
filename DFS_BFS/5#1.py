from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
path = [[] for _ in range(n+1)]
visited = [[False] for _ in range(n+1)]
visited[x] = True
answer = []
distance = 0

for _ in range(m):
    start, end = map(int, input().split())
    path[start].append(end)
queue = deque()
queue.append((x, distance))

while queue:
    v, d = queue.popleft()
    if d == k:
        answer.append(v)
    if d > k:
        continue
    distance += 1
    for city in path[v]:
        if visited[city] == [False]:
            queue.append((city, distance))
            visited[city] = True
            
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)