from collections import deque

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = 0

def get_next(robot, board):
    [x_l, y_l], [x_r, y_r] = robot
    next = []
    for i in range(len(dx)):
        if board[x_l+dx[i]][y_l+dy[i]] != 1 and board[x_r+dx[i]][y_r+dy[i]] != 1:
            next.append({(x_l+dx[i], y_l+dy[i]), (x_r+dx[i], y_r+dy[i])})
    #블록이 가로로
        if x_l == x_r:
            if board[x_l+1][y_l] == 0 and board[x_r+1][y_r] == 0:
                next.append({(x_l,y_l), (x_l+1, y_l)})
                next.append({(x_r+1, y_r), (x_r,y_r)})
            if board[x_l-1][y_l] == 0 and board[x_r-1][y_r] == 0:
                next.append({(x_l,y_l), (x_l-1, y_l)})
                next.append({(x_r-1, y_r), (x_r,y_r)})

        #블록이 세로로
        elif y_l == y_r:
            if board[x_l][y_l+1] == 0 and board[x_r][y_r+1] == 0:
                next.append({(x_l,y_l), (x_l,y_l+1)})
                next.append({(x_r,y_r+1), (x_r,y_r)})
            if board[x_l][y_l-1] == 0 and board[x_r][y_r-1] == 0:
                next.append({(x_l,y_l), (x_l,y_l-1)})
                next.append({(x_r,y_r-1), (x_r,y_r)})  
    return next

def solution(board):
    q = deque()
    robot = {(1,1), (1,2)}
    global N
    N = len(board)
    new_board = [[1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    q.append((robot, 0))
    visited = []
    visited.append(robot)

    while q:
        pos, time = q.popleft()
        print(pos, time)
        if (N,N) in pos:
            return time
        else:
            for next in get_next(pos, new_board):
                if next not in visited:
                    visited.append(next)
                    q.append((next, time+1))

print(solution(	[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))