import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board = []
iceberg = []
years = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] != 0:
            iceberg.append([i,j])
    board.append(tmp)

def in_range(x, y):
    if x in range(N) and y in range(M):
        return True
    return False

def bfs():
    count = 0
    queue = deque([iceberg[0]])
    visited = [[0]*M for _ in range(N)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_range(nx, ny) and board[nx][ny] != 0 and visited[nx][ny] == 0:
                count += 1
                visited[nx][ny] = 1
                queue.append([nx, ny])
    
    if count == len(iceberg):
        return True
    else:
        return False

while True:
    #2개로 분리됐는지 ?
    if len(iceberg) == 0:
        break
    if bfs():
        years += 1
        melted = [[0]*M for _ in range(N)]
        j = 0
        while j < len(iceberg):
            x, y = iceberg[j]
            #네방향 중 바다인 부분 체크
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if in_range(nx, ny) and board[nx][ny] == 0 and melted[nx][ny] != 1:
                    board[x][y] -= 1
                    if board[x][y] == 0:
                        melted[x][y] = 1
                        iceberg.remove([x,y])
                        j -= 1
                        break
            j += 1
    else:
        break
if len(iceberg) == 0:
    print(0)
else:
    print(years)