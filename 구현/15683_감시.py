import sys
import copy
from collections import deque

input = sys.stdin.readline

#상좌하우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def in_bound(x, y):
    if x in range(N) and y in range(M):
        return True
    return False

def check(num, board, d, x, y):
    nx, ny = x+dx[d], y+dy[d]
    while in_bound(nx, ny):
        if board[nx][ny] != 6:
            if board[nx][ny] == 0:
                board[nx][ny] = "#"
            nx, ny = nx+dx[d], ny+dy[d]
        else:
            break
    
    if num == 3 or num == 4 or num == 5:
        nx, ny = x+dx[(d+1)%4], y+dy[(d+1)%4]
        while in_bound(nx, ny):
            if board[nx][ny] != 6:
                if board[nx][ny] == 0:
                    board[nx][ny] = "#"
                nx, ny = nx+dx[(d+1)%4], ny+dy[(d+1)%4]
            else:
                break
    
    if num == 2 or num == 5:
        nx, ny = x+dx[(d+2)%4], y+dy[(d+2)%4]
        while in_bound(nx, ny):
            if board[nx][ny] != 6:
                if board[nx][ny] == 0:
                    board[nx][ny] = "#"
                nx, ny = nx+dx[(d+2)%4], ny+dy[(d+2)%4]
            else:
                break
    
    if num == 4 or num == 5:
        nx, ny = x+dx[(d+3)%4], y+dy[(d+3)%4]
        while in_bound(nx, ny):
            if board[nx][ny] != 6:
                if board[nx][ny] == 0:
                    board[nx][ny] = "#"
                nx, ny = nx+dx[(d+3)%4], ny+dy[(d+3)%4]
            else:
                break

def bfs(board, cctv):
    queue = deque([(board, cctv)])
    global minval
    while queue:
        b, c = queue.popleft()
        if not c:
            count = 0
            for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j] == 0:
                        count += 1
            minval = min(minval, count)
        else:
            cnum, x, y = c.popleft()
            if cnum in [1, 3, 4]:
                # 4방향에 대해 체크
                for i in range(4):
                    nb = copy.deepcopy(b)
                    nc = copy.deepcopy(c)
                    check(cnum, nb, i, x, y)
                    queue.append((nb, nc))
            elif cnum == 2:
                # 2방향에 대해 체크
                for i in range(2):
                    nb = copy.deepcopy(b)
                    nc = copy.deepcopy(c)
                    check(cnum, nb, i, x, y)
                    queue.append((nb, nc))
            else:
                # 한방향에 대해 체크
                nb = copy.deepcopy(b)
                nc = copy.deepcopy(c)
                check(cnum, nb, 0, x, y)
                queue.append((nb, nc))

N, M = map(int, input().split())
minval = N*M
board = []
cctv = deque()
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] in range(1, 6):
            cctv.append((tmp[j], i, j))
    board.append(tmp)
bfs(board, cctv)
print(minval)