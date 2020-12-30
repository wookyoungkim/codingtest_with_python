import sys
import copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
answer = 0
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def in_bound(x, y):
    if x in range(0,N) and y in range(0,N):
        return True
    else:
        return False

def move(board, dir):
    merged = [[0]*N for _ in range(N)]
    if dir % 2 == 0:
        start, end, inc = 0, N, 1
    else:
        start, end, inc = N-1, -1, -1
    # 각각의 칸에 대해서
    for i in range(start, end, in1c):
        for j in range(start, end, inc):
            if board[i][j] != 0:
                x, y = i, j
                nx, ny = x + dx[dir], y + dy[dir]
                while in_bound(nx, ny):
                    # 빈칸이면
                    if board[nx][ny] == 0:
                        board[nx][ny] = board[x][y]
                        board[x][y] = 0
                        x, y = nx, ny
                        nx, ny = x + dx[dir], y + dy[dir]
                    # 같은 숫자를 만나면
                    elif board[nx][ny] == board[x][y]:
                        if not merged[nx][ny]:
                            board[nx][ny] += board[x][y]
                            board[x][y] = 0
                            merged[nx][ny] = 1
                        break
                    # 다른 숫자를 만나면
                    else:
                        break
    

def dfs(board, count):
    #print(count, board)
    global answer
    if count >= 5:
        max_val = 0
        for i in range(N):
            max_val = max(max_val, max(board[i]))
        answer = max(answer, max_val)
        return
    for i in range(4):
        new_board = copy.deepcopy(board)
        move(new_board, i)
        #이동 가능하면
        if new_board != board:
            dfs(new_board, count+1)
        #더 이상 이동이 불가능하면 -> 최대값 갱신 
        else:
            max_val = 0
            for j in range(N):
                max_val = max(max_val, max(board[j]))
            answer = max(answer, max_val)


dfs(board, 0)
print(answer)
