import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
islands = [[]*(N+1) for _ in range(N+1)]

#양방향 그래프로 저장하기
for _ in range(M):
    island_A, island_B, weight = map(int, input().split())
    islands[island_A].append([island_B, weight])
    islands[island_B].append([island_A, weight])
departure, destination = map(int, input().split())

def bfs(mid):
    queue = deque([departure])
    visit[departure] = 1

    while queue:
        start = queue.popleft()
        if start == destination:
            return True
        for island_B, weight in islands[start]:
            if visit[island_B] == 0 and mid <= weight:
                queue.append(island_B)
                visit[island_B] = 1
    return False

#이분탐색 -> 대상 : 무게
min_val, max_val = 1, 1000000000
while min_val <= max_val:
    visit = [0 for _ in range(N+1)]
    mid = (min_val+max_val)//2
    #해당 무게로 이동 가능하면 무게 늘리기
    if bfs(mid):
        min_val = mid + 1
    else:
        max_val = mid - 1
print(max_val)