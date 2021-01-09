import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = []
dp = [[-1]*M for _ in range(N)]
dp[0][0] = 1

for _ in range(N):
    board.append(list(map(int, input().split())))

def in_range(x, y):
    if x in range(N) and y in range(M):
        return True
    return False

def dfs(x, y):
    if x == 0 and y == 0:
        return dp[x][y]
    #방문하지 않은 칸에 대해서
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_range(nx, ny) and board[nx][ny] > board[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(N-1,M-1))