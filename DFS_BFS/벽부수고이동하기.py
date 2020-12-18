import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
map_pos = []

N, M = map(int, input().split())

for _ in range(N):
    map_pos.append(list(map(int, input().strip())))

def in_bound(x,y):
    if x in range(0, N) and y in range(0, M):
        return True
    else:
        return False

def bfs(map_pos):
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    #(x,y), 벽 부셨는지?
    queue = deque([[(0,0),0]])
    visited[0][0][0] = 1
    while queue:
        (x,y),flag = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][flag]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if in_bound(nx, ny):
                #빈칸일때
                if map_pos[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    queue.append([(nx,ny), flag])
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                #벽일때
                else:
                    if flag == 0:
                        queue.append([(nx,ny), 1])
                        visited[nx][ny][1] = visited[x][y][0] + 1
    return -1
print(bfs(map_pos))
