#우, 하, 우상, 좌하
dx = [0, 1, -1, 1]
dy = [1, 0, 1, -1]

def in_board(x,y,n):
    if 0<=x<n and 0<=y<n:
        return True
    else: return False

def solution(n, horizontal):
    board = [[0]*n for _ in range(n)]
    
    x, y = 0, 0
    dir = 0 if horizontal is True else 1
    time = 0
    
    while [x, y] != [n-1, n-1]:
        #print(x,y,dir,time)
        board[x][y] = time
        #방향대로 이동한다
        x += dx[dir]
        y += dy[dir]
        
        if dir == 0 or dir == 1: #수평, 수직이동
            time += 1
            if in_board(x+dx[2], y+dy[2], n):
                dir = 2
            else: dir = 3
        else: #대각선 이동
            time += 2
            if in_board(x+dx[dir], y+dy[dir], n) == False:
                #방향 벗어나면
                if dir == 2: #우상
                    if in_board(x+dx[0], y+dy[0], n):
                        dir = 0
                    else:
                        dir = 1
                else: #좌하
                    if in_board(x+dx[1], y+dy[1], n):
                        dir = 1
                    else:
                        dir = 0
    board[n-1][n-1] = time
                
    return board

print(solution(100,	False))