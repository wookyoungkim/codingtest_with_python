from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

#이동방향 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    print(x,y, "->")
    while(queue):
        x,y = queue.popleft()
        #현재 위치에서 네방향 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx,ny))
                print(maze[nx][ny], " : " ,nx,ny,"->")
                print(queue)
    #출구까지의 거리 반환
    return maze[n-1][m-1]

print(bfs(0,0))