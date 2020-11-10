from collections import deque
import sys

input = sys.stdin.readline
n,l,r = map(int, input().split())

worldmap = []
for _ in range(n):
    worldmap.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    #(x,y)와 연결된 연합 정보 담기
    united = []
    united.append((x,y))

    #BFS로 연결된 연합 확인
    q = deque()
    q.append((x,y))
    union[x][y] = index
    #연합의 인구수
    population = worldmap[x][y]
    #연합에 속한 나라 수
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #연합에 속할 조건 만족하는지?
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l<= abs(worldmap[x][y] - worldmap[nx][ny]) <=r:
                    q.append((nx,ny))
                    union[nx][ny] = index
                    population += worldmap[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i,j in united:
        worldmap[i][j] = population//count

total_count = 0

while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j, index)
                index += 1
    #모든 인구이동 후
    #print(union)
    if index == n*n:
        break
    total_count += 1

print(total_count)