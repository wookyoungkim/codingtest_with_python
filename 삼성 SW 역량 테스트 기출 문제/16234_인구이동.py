import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, L, R = map(int, input().split())
countries = []
answer = 0
for _ in range(N):
    countries.append(list(map(int, input().split())))

def in_range(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

def check_union(x, y, nx, ny):
    if abs(countries[x][y] - countries[nx][ny]) in range(L, R+1):
        return True
    return False

def bfs(x, y, index):
    queue = deque([(x,y)])
    union = [(x, y)]
    total = countries[x][y]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_range(nx, ny) and check_union(x, y, nx, ny) and united[nx][ny] == -1:
                queue.append((nx, ny))
                union.append((nx, ny))
                united[nx][ny] = 1
                total += countries[nx][ny]
    
    population = total//len(union)
    for x, y in union:
        countries[x][y] = population

while True:
    united = [[-1]*N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            #아직 합쳐지지 않은 나라에 대해서
            if united[i][j] == -1:
                united[i][j] = index
                bfs(i, j, index)
                index += 1
    if index == N*N:
        break
    answer += 1

print(answer)