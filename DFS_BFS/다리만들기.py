import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
Map = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
islands = {}
answer = N*N+1

for i in range(N):
    Map.append(list(map(int, input().split())))

def in_bound(x,y):
    if x in range(0,N) and y in range(0,N):
        return True
    else:
        return False

def bfs(i,j,count):
    Map[i][j] = count
    queue = deque([(i,j)])
    while queue:
        x,y = queue.popleft()
        Map[x][y] = count

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if in_bound(nx, ny):
                if Map[nx][ny] == 1:
                    queue.append((nx,ny))

#지도에서 각 섬 표시
def find_islands(Map):
    count = 2
    for i in range(len(Map)):
        for j in range(len((Map[0]))):
            if Map[i][j] == 1:
                bfs(i,j,count)
                count += 1

def check_diff_island(x1,y1,x2,y2):
    visited = [[0]*N for _ in range(N)]
    queue = deque([(x1,y1)])
    visited[x1][y1] = 1
    while queue:
        x,y = queue.popleft()
        if x == x2 and y == y2:
            return False
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_bound(nx,ny):
                if Map[nx][ny] == 1 and visited[nx][ny] != 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    return True

def set_bridge(i,j):
    visited = [[0]*N for _ in range(N)]
    queue = deque([(i,j)])
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if in_bound(nx,ny):
                #다른땅에 도착하면
                if Map[nx][ny] != 0 and check_diff_island(nx,ny, i,j):
                    return visited[x][y]
                #바다고 아직 방문한적 없으면
                if Map[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return N*N+1
#섬 별로 분리하기
#find_islands(Map)

for i in range(len(Map)):
    for j in range(len(Map[0])):
        #섬이면
        if Map[i][j] != 0:
            answer = min(answer, set_bridge(i,j))
print(answer)