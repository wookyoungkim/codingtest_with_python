import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_bound(x, y):
    if x in range(0, R) and y in range(0, C):
        return True
    else:
        return False

def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_bound(nx, ny):
            if path[ord(Map[nx][ny]) - 65] != 1:
                path[ord(Map[nx][ny]) - 65] = 1
                dfs(nx, ny, count+1)
                path[ord(Map[nx][ny]) - 65] = 0

R, C = map(int, input().split())
Map = []

for _ in range(R):
    Map.append(list(input().strip()))

answer = 1
path = [0]*26
path[ord(Map[0][0]) - 65] = 1
dfs(0, 0, answer)
print(answer)
