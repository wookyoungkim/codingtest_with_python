import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input()) #보드의 크기
board = [[0]*N for _ in range(N)]
K = int(input()) #사과의 개수
for _ in range(K):
    apples_x, apples_y = map(int, input().split())
    board[apples_x-1][apples_y-1] = 2
L = int(input()) #회전 횟수
directions = {}
for _ in range(L):
    t, d = input().split()
    directions[int(t)] = d
time = 0
snake = [[0,0]]
board[0][0] = 1
dirc = 3

while True:
    #방향 이동이 있으면
    if time in directions.keys():
        dir = directions[time]
        if dir == 'L':
            dirc = (dirc+1)%4
        else:
            dirc = (dirc+3)%4
    time += 1
    #머리 이동시키기
    nx, ny = snake[-1][0]+dx[dirc], snake[-1][1]+dy[dirc]
    #다음 칸이 벽이나 뱀이면
    if not (0<=nx<N and 0<=ny<N) or [nx, ny] in snake:
        break
    #다음 칸이 빈칸면
    elif board[nx][ny] == 0:
        board[snake[0][0]][snake[0][1]] = 0
        snake.pop(0)
    board[nx][ny] = 1
    snake.append([nx,ny])

print(time)
    