# d[x][y][dir] : dir방향으로 (x,y)까지 도달할 수 있는 경우의 수
# 가로 : d[x][y][0] = d[x][y-1][0] + d[x][y-1][2]
# 세로 : d[x][y][1] = d[x-1][y][1] + d[x-1][y][2]
# 대각선 : d[x][y][2] = d[x-1][y-1][0] + d[x-1][y-1][1] + d[x-1][y-1][2]

import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
pipe = [0,1]
pipe_dir = 0 #0:가로, 1:세로, 2:대각선
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][0][0] = 1
dp[0][1][0] = 1

for x in range(N):
    for y in range(2, N):
        #대각선으로 이동
        if board[x][y-1] == board[x-1][y] == board[x][y] == 0:
            dp[x][y][2] = dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
        
        if board[x][y] == 0:
            #가로로 이동
            dp[x][y][0] = dp[x][y-1][0] + dp[x][y-1][2]
            #세로로 이동
            dp[x][y][1] = dp[x-1][y][1] + dp[x-1][y][2]

print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])
