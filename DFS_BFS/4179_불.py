import sys
from collections import deque
import copy

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
maze = []
jihoon = deque()
fire = deque()

for i in range(R):
    tmp = list(input().strip())
    for j in range(C):
        if tmp[j] == 'J':
            jihoon.append((i,j))
        elif tmp[j] == 'F':
            fire.append((i,j))
    maze.append(tmp)

def in_range(x, y):
    if x in range(R) and y in range(C):
        return True
    return False

# fire[i] : i초 뒤 불의 확산좌표들 저장
def move_fire():
    tmp = set()
    for x, y in fire[-1]:
        for i in range(4):
            fx, fy = x+dx[i], y+dy[i]
            if in_range(fx, fy) and maze[fx][fy] != '#':
                tmp.add((fx, fy))
            tmp.add((x, y))
    fire.append(list(tmp))

def bfs():
    time = 0
    while jihoon:
        #불 확산시키기
        for _ in range(len(fire)):
            x, y = fire.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if in_range(nx, ny) and (maze[nx][ny] == '.' or maze[nx][ny] == 'J') :
                    maze[nx][ny] = 'F'
                    fire.append((nx,ny))

        #지훈이 이동
        for _ in range(len(jihoon)):
            x, y = jihoon.popleft()
            if x == 0 or x == R-1 or y == 0 or y == C-1:
                return time+1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if in_range(nx, ny) and maze[nx][ny] == '.':
                    maze[nx][ny] = 'J'
                    jihoon.append((nx, ny))
        time += 1
    return -1

answer = bfs()
if answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer)
