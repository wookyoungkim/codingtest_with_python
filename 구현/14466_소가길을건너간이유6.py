import sys
from collections import defaultdict, deque
import copy

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, K, R = map(int, input().split())
roads = [[[] for _ in range(N)] for _ in range(N)]
cows = [[0 for _ in range(N)] for _ in range(N)]
cow_list = []
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    roads[r1-1][c1-1].append([r2-1, c2-1])
    roads[r2-1][c2-1].append([r1-1, c1-1])

for _ in range(K):
    r, c = map(int, input().split())
    cows[r-1][c-1] = 1
    cow_list.append((r-1, c-1))
num_cows = len(cow_list)

def in_bound(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

def bfs(cow):
    # cow가 길을 건너지 않고 만날 수 있는 소의 개수
    queue = deque()
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[cow[0]][cow[1]] = True
    queue.append([cow[0], cow[1]])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_bound(nx, ny) and visited[nx][ny] == 0:
                if roads[x][y] == [] or [nx,ny] not in roads[x][y]:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    if cows[nx][ny] == 1:
                        count += 1
    # 전체 소 - 현재 소 - 길안건너고 만날 수 있는 소 = 길 건너야만 만나는 소
    return num_cows - 1 - count          
    
answer = 0
for cow in cow_list:
    answer += bfs(cow)
    cows[cow[0]][cow[1]] = 0
    num_cows -= 1
    
print(answer)