import sys
from collections import deque
import copy

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
board = []
for _ in range(N):
    # -2:빈칸 -1:검은색 0:무지개색 1~:일반
    board.append(list(map(int, input().split())))

def in_bound(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

def findBlockGroup(i, j):
    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue.append([i,j])
    visited[i][j] = True
    block = [[i,j]]

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if in_bound(nx, ny) and not visited[nx][ny] and (board[nx][ny] == board[i][j] or board[nx][ny] == 0):
                visited[nx][ny] = True
                queue.append([nx,ny])
                block.append([nx,ny])
    return block

def move():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if board[i][j] > 0:
                x, y = i, j
                while True:
                    nx, ny = x+1, y
                    if in_bound(nx, ny) and board[nx][ny] == -2:
                        board[nx][ny] = board[x][y]
                        board[x][y] = -2
                        x, y = nx, ny
                    else:
                        break
    
def rotate_anticlockwise():
    new_board = copy.deepcopy(board)
    for i in range(N):
        for j in range(N):
            board[N-j-1][i] = new_board[i][j]

answer = 0
while True:
    # 1. 제일 큰 블록 찾기
    max_block = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                block = findBlockGroup(i,j)
                if len(block) > len(max_block) and len(block) > 1:
                    max_block = block
    
    if max_block == []:
        # 찾을 수 있는 블록 집합이 없으면
        break
    # 1.1 block 없애기
    for b in max_block:
        board[b[0]][b[1]] = -2
    # 1.2 점수 획득
    answer += len(max_block)*len(max_block)
    
    # 2. 이동시키기
    move()

    # 3. 반시계방향으로 90도 회전
    rotate_anticlockwise()

    # 4. 이동시키기
    move()