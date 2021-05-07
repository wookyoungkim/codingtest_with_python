import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, Q = map(int, input().split())
board = []
for _ in range(2**N):
    board.append(list(map(int, input().split())))
Levels = list(map(int, input().split()))

def rotate_90(parts):
    return list(zip(*parts[::-1]))

def in_bound(x, y):
    if x in range(2**N) and y in range(2**N):
        return True
    return False

def bfs(x, y, visited):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_bound(nx,ny) and not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append([nx, ny])
                count += 1
    return count

for L in Levels:
    # 1. 2^L * 2^L로 나누기
    for i in range(0, 2**N, 2**L):
        for j in range(0, 2**N, 2**L):
            parts = []
            for k in range(2**L):
                parts.append(board[k+i][j:j+2**L])
            # 2. 90도 회전
            rotated = rotate_90(parts)
            for k in range(2**L):
                board[k+i][j:j+2**L] = rotated[k]
    
    # 3.얼음의 양 줄이기
    decrement = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            if board[i][j] > 0:
                count = 0
                for d in range(4):
                    ni, nj = i+dx[d], j+dy[d]
                    if in_bound(ni, nj):
                        if board[ni][nj] > 0:
                            count += 1
                if count < 3:
                    decrement[i][j] = -1
    for i in range(2**N):
        for j in range(2**N):
            board[i][j] += decrement[i][j]
                      
# 남은 얼음합
answer1 = 0
for i in range(2**N):
    answer1 += sum(board[i])
    
visited = [[False for _ in range(2**N)] for _ in range(2**N)]
answer2 = 0
for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and board[i][j] > 0:
            answer2 = max(answer2, bfs(i,j,visited))

print(answer1)
print(answer2)