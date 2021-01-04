import sys

input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

N, M, x, y, K = map(int, input().split())
board = []
dice = [0]*7
opposite = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
top, east, north = 1, 3, 2
answer = []

for i in range(N):
    board.append(list(map(int, input().split())))

moves = list(map(int, input().split()))

def in_range(x, y):
    if x in range(N) and y in range(M):
        return True
    else:
        return False

for move in moves:
    #다음 칸으로 이동
    nx, ny = x+dx[move], y+dy[move]
    #지도를 벗어나면 해당 명령 무시하기
    if in_range(nx, ny) == False:
        continue

    #주사위 이동하기
    if move == 1:
        #동쪽이면
        top, east = opposite[east], top
    elif move == 2:
        #서쪽이면
        top, east = east, opposite[top]
    elif move == 3:
        # 북쪽이면
        top, north = opposite[north], top
    else:
        #남쪽이면
        top, north = north, opposite[top]

    if board[nx][ny] == 0:
        board[nx][ny] = dice[opposite[top]]
    else:
        dice[opposite[top]] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny
    print(dice[top])