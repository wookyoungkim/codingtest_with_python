import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

N, M, H = map(int, input().split())
board = [[0] * N for _ in range(H)]
minval = 4
ladders = set()

for i in range(M):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

def play(board):
    for start in range(N):
        cur_y = start
        for cur_x in range(H):
            if board[cur_x][cur_y] == 1:
                cur_y += 1
            elif cur_y > 0 and board[cur_x][cur_y-1] == 1:
                cur_y -= 1
        if start != cur_y:
            return False
    return True

def dfs(count, x, y):
    global minval
    if play(board):
        minval = min(minval, count)
        return
    if count == 3 or minval <= count:
        return
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N-1):
            if board[i][j] == 0 and board[i][j+1] == 0:
                board[i][j] = 1
                dfs(count+1, i, j+2)
                board[i][j] = 0
            
dfs(0, 0,0)

if minval == 4:
    print(-1)
else:
    print(minval)