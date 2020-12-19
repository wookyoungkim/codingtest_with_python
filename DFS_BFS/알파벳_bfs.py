import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C = map(int, input().split())
Map = []

for _ in range(R):
    Map.append(list(input().strip()))

answer = 1

def in_bound(x, y):
    if x in range(0, R) and y in range(0, C):
        return True
    else:
        return False

def bfs(x,y):
    global answer
    queue = deque([[x,y, Map[x][y]]])
    
    while queue:
        #print(queue)
        x, y, path = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_bound(nx, ny):
                if Map[nx][ny] not in path and [nx, ny, path+Map[nx][ny]] not in queue:
                    queue.append([nx, ny, path+Map[nx][ny]])
                    answer = max(answer, len(path)+1)

bfs(0,0)
print(answer)