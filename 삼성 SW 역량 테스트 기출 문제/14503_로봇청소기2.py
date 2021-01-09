import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
x, y, dir = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def in_range(x, y):
    if x in range(N) and y in range(M):
        return True
    return False

answer = 0

while 1:
    #clean
    if board[x][y] == 0:
        board[x][y] = 2
        answer += 1
    clean_flag = 0
    #check from left
    for i in range(4):
        next_dir = (dir+3)%4
        nx, ny = x+dx[next_dir], y+dy[next_dir]
        if in_range(nx, ny) and board[nx][ny] == 0:
            #in range and has not been cleaned
            dir = next_dir
            x, y = nx, ny
            clean_flag = 1
            break
        else:
            dir = next_dir
    if clean_flag == 1:
        continue
    else:
        behind = (dir+2)%4
        bx, by = x+dx[behind], y+dy[behind]
        if board[bx][by] == 1:
            # if all 4 spaces are cleaned and behind is wall
            break
        else:
            x, y = bx, by

print(answer)