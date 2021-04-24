import sys
from collections import defaultdict

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
reverse = {1:2, 2:1, 3:4, 4:3}
input = sys.stdin.readline

N, k = map(int, input().split())
board_color = []
for _ in range(N):
    board_color.append(list(map(int, input().split())))
horses = defaultdict()
horse_on_board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(k):
    x, y, d = map(int, input().split())
    horses[i] = [x-1, y-1, d]
    horse_on_board[x-1][y-1].append(i)

def in_bound(x,y):
    if x in range(N) and y in range(N):
        return True
    return False

def move_white(h):
    x, y, d = horses[h]
    nx, ny = x+dx[d], y+dy[d]
    idx = horse_on_board[x][y].index(h)
    if len(horse_on_board[nx][ny]) + len(horse_on_board[x][y][idx:]) >= 4:
        return False
    for moving in horse_on_board[x][y][idx:]:
        horses[moving][0] = nx
        horses[moving][1] = ny
    horse_on_board[nx][ny] += horse_on_board[x][y][idx:]
    horse_on_board[x][y] = horse_on_board[x][y][:idx]
    return True

def move_red(h):
    x, y, d = horses[h]
    nx, ny = x+dx[d], y+dy[d]
    idx = horse_on_board[x][y].index(h)
    if len(horse_on_board[nx][ny]) + len(horse_on_board[x][y][idx:]) >= 4:
        return False
    for moving in horse_on_board[x][y][idx:]:
        horses[moving][0] = nx
        horses[moving][1] = ny
    horse_on_board[nx][ny] += list(reversed(horse_on_board[x][y][idx:]))
    horse_on_board[x][y] = horse_on_board[x][y][:idx]
    return True

def move_blue(h):
    flag = True
    x, y, d = horses[h]
    horses[h][2] = reverse[d]
    nx, ny = x+dx[horses[h][2]], y+dy[horses[h][2]]
    if in_bound(nx, ny) and board_color[nx][ny] != 2:
        # 범위를 벗어나지 않고 파란 칸이 아니면
        if board_color[nx][ny] == 0:
            flag = move_white(h)
        else:
            flag = move_red(h)
    return flag

count = 1
while True:
    flag = True
    if count > 1000:
        break
    for h in horses.keys():
        # 모든 말에 대해서 이동
        x, y, d = horses[h]
        nx, ny = x+dx[d], y+dy[d]

        if in_bound(nx, ny):
            if board_color[nx][ny] == 0:
                # 흰색이면
                if move_white(h) == False:
                    flag = False
                    break
            elif board_color[nx][ny] == 1:
                # 빨간색이면
                if move_red(h) == False:
                    flag = False
                    break
            else:
                # 파란색이면
                if move_blue(h) == False:
                    flag = False
                    break
        else:
            # 방향 바꾸고 한칸 이동
            if move_blue(h) == False:
                flag = False
                break
    if flag == False:
        break
    count += 1
if count > 1000:
    print(-1)
else:
    print(count)