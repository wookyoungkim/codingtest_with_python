import sys
from collections import deque, defaultdict

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def in_range(x, y):
    if x in range(n) and y in range(m):
        return True
    return False

def find_island(x, y, num):
    queue = deque([(x, y)])
    board[x][y] = num

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_range(nx, ny) and board[nx][ny] == 1:
                board[nx][ny] = num
                queue.append((nx,ny))

def next_to_sea(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_range(nx, ny) and board[nx][ny] == 0:
            return True
    return False

def find_bridge(islandnum, x, y):
    queue = deque([(x, y, 0, 0), (x, y, 1, 0), (x, y, 2, 0), (x, y, 3, 0)])
    visited = [[False]*m for _ in range(n)]

    while queue:
        #한방향으로만 쭉 이동
        x, y, dir, count = queue.popleft()

        nx, ny = x+dx[dir], y+dy[dir]
        if in_range(nx, ny) and not visited[nx][ny]:
            #바다면
            if board[nx][ny] == 0:
                queue.append((nx, ny, dir, count+1))
            #다른 섬이면
            elif board[nx][ny] != islandnum:
                if count > 1:
                    is_a = min(board[nx][ny], islandnum)
                    is_b = max(board[nx][ny], islandnum)
                    if (is_a, is_b) in distance.keys():
                        distance[(is_a, is_b)] = min(distance[(is_a, is_b)], count)
                    else:
                        distance[(is_a, is_b)] = count

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    global connected
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    connected += 1
    
                
# 섬끼리 구분짓기
num = 2
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            find_island(i, j, num)
            num += 1
distance = {}
#섬끼리 연결하기
for i in range(n):
    for j in range(m):
        #땅이면
        if board[i][j] != 0 and next_to_sea(i,j):
            #바다 옆이면
            find_bridge(board[i][j], i, j)

# 크루스칼로 섬들끼리 연결하는 최소 비용 찾기
edges = []
connected = 0
result = 0
parent = [0] * num

for i in range(1, num):
    parent[i] = i

for key, val in distance.items():
    edges.append((val, key))

edges.sort()

for edge in edges:
    cost, (a, b) = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


if connected == num -3:
    print(result)
else:
    print(-1)