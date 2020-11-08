from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  

def move(x, y, dir, n):
        x += dx[dir]
        if x >= n: #아래로 넘어가면
            x = 0
        elif x < 0: #위로 넘어가면
            x = n-1

        y += dy[dir]
        if y >= n: #오른쪽으로 넘어가면
            y = 0
        elif y < 0: #왼쪽으로 넘어가면
            y = n-1
        return x,y 

def bfs(board, x,y, final, n): 
    print(board[x][y], " to ", final, end=": ")
    queue = deque()
    count = 0
    queue.append((x,y,count))

    while queue:
        x,y,count = queue.popleft()
        print(x,y, board[x][y])
        if board[x][y] == final:
            break
        for i in range(4):
            d_x, d_y = move(x,y,i, n)
            if (d_x, d_y) not in queue:
                queue.append((d_x, d_y, count+1))
    return x,y,count + 1

def solution(n, board):
    answer = 0
    cur_x, cur_y = 0, 0
    for i in range(1, n*n+1):
        cur_x, cur_y, ans = bfs(board, cur_x, cur_y, i, n)
        answer += ans
    return answer

print(solution(2,	[[2, 3], [4, 1]]))