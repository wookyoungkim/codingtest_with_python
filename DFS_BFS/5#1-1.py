from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
path = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
#출발도시~출발도시는 0
distance[x] = 0

for _ in range(m):
    start, end = map(int, input().split())
    path[start].append(end)

queue = deque([x])
while queue:
    v = queue.popleft()
    for city in path[v]:
        if distance[city] == -1:
            queue.append(city)
            distance[city] = distance[v]+1

#print(distance)
check = False
for i in range(1,len(distance)):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)