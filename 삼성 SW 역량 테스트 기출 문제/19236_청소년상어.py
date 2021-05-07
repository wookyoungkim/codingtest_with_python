import sys
from collections import defaultdict
import copy

input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# -1: 빈칸, 0: 상어, 나머지: 물고기 번호
board = [[-1 for _ in range(4)] for _ in range(4)]
fishes = defaultdict()
shark = [0,0]
answer = 0

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        n, d = tmp[2*j], tmp[2*j+1]
        fishes[n] = [i,j,d, True]
        board[i][j] = n
        if i==0 and j==0:
            shark.append(d)
            answer = n

# 상어의 초기 이동
del(fishes[board[0][0]])
board[0][0] = 0

def in_bound(x, y):
    if x in range(4) and y in range(4):
        return True
    return False

def move_fishes(board, fishes):
    c_board = copy.deepcopy(board)
    cur_fish = sorted(fishes.keys())

    for f in cur_fish:
        x, y, d, flag = fishes[f]
        # 이번 turn에 살아있는 물고기면
        if flag == True:
            for i in range(8):
                nx, ny = x+dx[d-1], y+dy[d-1]
                if in_bound(nx, ny) and c_board[nx][ny] != 0:
                    # 범위 안이고 상어있는 칸이 아니면
                    if c_board[nx][ny] == -1:
                        # 빈칸이면 그냥 이동
                        c_board[nx][ny] = f
                        c_board[x][y] = -1
                        fishes[f][0], fishes[f][1], fishes[f][2] = nx, ny, d
                        break
                    else:
                        # 빈칸이 아니면 교환
                        n_f = c_board[nx][ny]
                        c_board[nx][ny] = f
                        c_board[x][y] = n_f
                        fishes[f][0], fishes[f][1], fishes[f][2] = nx, ny, d
                        fishes[n_f][0], fishes[n_f][1] = x, y
                        break
                else:
                    d = (d+1)%8
    return c_board

def dfs(board, shark, fishes, count):
    global answer

    # 1. 물고기의 이동
    n_fishes = copy.deepcopy(fishes)
    c_board = move_fishes(board, n_fishes)

    # 2. 상어 이동
    x, y, d = shark
    while True:
        nx, ny = x+dx[d-1], y+dy[d-1]
        if not in_bound(nx, ny):
            break
        
        if c_board[nx][ny] != -1:
            # 빈칸이 아니면 물고기 먹고 그 칸으로 이동
            f_n = c_board[nx][ny]
            n_fishes[f_n][3] = False
            c_board[nx][ny] = 0
            c_board[shark[0]][shark[1]] = -1
            dfs(c_board, [nx, ny, n_fishes[f_n][2]], n_fishes, count+f_n)
            c_board[shark[0]][shark[1]] = 0
            c_board[nx][ny] = f_n
            n_fishes[f_n][3] = True

        x, y = nx, ny
                
    answer = max(answer, count)

dfs(board, shark, fishes, answer)
print(answer)