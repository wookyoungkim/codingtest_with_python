import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Map = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited_rgb = [[0]*N for _ in range(N)]
visited_rg = [[0]*N for _ in range(N)]

for _ in range(N):
    Map.append(list(input().strip()))

def in_bound(x,y):
    if x in range(0,N) and y in range(0,N):
        return True
    else:
        return False

def check_rg(rgb1, rgb2):
    if rgb1 == rgb2:
        return True
    elif rgb1 in ('R', 'G') and rgb2 in ('R', 'G'):
        return True
    else:
        return False

def region_for_rgb(i,j):
    queue = deque([(i,j)])
    visited_rgb[i][j] = 1

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if in_bound(nx, ny):
                if visited_rgb[nx][ny] == 0 and Map[nx][ny] == Map[x][y]:
                    queue.append((nx, ny))
                    visited_rgb[nx][ny] = 1

def region_for_rg(i,j):
    queue = deque([(i,j)])
    visited_rg[i][j] = 1

    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if in_bound(nx, ny):
                if visited_rg[nx][ny] == 0 and check_rg(Map[nx][ny], Map[x][y]):
                    queue.append((nx, ny))
                    visited_rg[nx][ny] = 1

count_rgb = 0
count_rg = 0
for i in range(N):
    for j in range(N):
        if visited_rgb[i][j] == 0:
            region_for_rgb(i,j)
            count_rgb += 1
        if visited_rg[i][j] == 0:
            region_for_rg(i,j)
            count_rg += 1

print(count_rgb, count_rg)

    