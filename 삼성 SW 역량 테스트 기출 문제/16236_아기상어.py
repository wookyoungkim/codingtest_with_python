import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())
board = []
shark = []
shark_weight = 2
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 9:
            shark = [i,j]
    board.append(tmp)
board[shark[0]][shark[1]] = 0

def in_bound(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

def find(shark, d):
    visited = [[float('INF') for _ in range(N)] for _ in range(N)]
    queue = deque([[shark[0], shark[1]]])
    visited[shark[0]][shark[1]] = 0
    min_count, n_x, n_y = float('INF'), 0, 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_bound(nx, ny) and visited[x][y]+1 < visited[nx][ny]:
                if board[nx][ny] != 0 and board[nx][ny] < shark_weight:
                    # 작으면 이 물고기 먹기 -> 제일 위쪽 왼쪽에 있는거
                    if visited[x][y]+1 < min_count:
                        min_count = visited[x][y]+1
                        n_x, n_y = nx, ny
                        visited[nx][ny] = visited[x][y]+1
                    elif visited[x][y]+1 == min_count:
                        if n_x > nx:
                            n_x, n_y = nx, ny
                            visited[nx][ny] = visited[x][y]+1
                        elif n_x == nx and n_y > ny:
                            n_x, n_y = nx, ny
                            visited[nx][ny] = visited[x][y]+1
                elif board[nx][ny] == 0 or board[nx][ny] == shark_weight:
                    if visited[x][y]+1 > min_count:
                        break
                    else:
                        # 이동가능하면 이동
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx,ny])

    if min_count != float('inf'):
        return min_count, n_x, n_y            
    else:
        return -1, -1, -1

time = 0
eat = 0
while True:
    # 상어 이동하기
    count, x, y = find(shark, i)

    if count == -1:
        # 더 먹을 물고기 x
        break
    
    board[x][y] = 0
    shark = [x, y]
    eat += 1
    if eat == shark_weight:
        shark_weight += 1
        eat = 0
    time += count

print(time)