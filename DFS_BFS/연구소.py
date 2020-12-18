import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
lab = []
virus_pos = []
empty_pos = []
answer = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 0:
            empty_pos.append((i,j))
        elif tmp[j] == 2:
            virus_pos.append((i,j))
    lab.append(tmp)

def in_boundary(x,y):
    if x in range(0, N) and y in range(0,M):
        return True
    else:
        return False

def bfs(lab, virus_pos):
    #모든 바이러스의 위치를 queue에
    queue = deque(virus_pos)
    while queue:
        #각 바이러스에서
        x, y = queue.popleft()
        #상하좌우 검사
        for i in range(4):
            #범위 내에 있고 빈칸이면
            if in_boundary(x+dx[i], y+dy[i]):
                if lab[x+dx[i]][y+dy[i]] == 0:
                    #바이러스 퍼뜨리기 
                    lab[x+dx[i]][y+dy[i]] = 2
                    queue.append((x+dx[i], y+dy[i]))
    count = 0
    for i in range(N):
        count += lab[i].count(0)
    for x,y in empty_pos:
        lab[x][y] = 0
    return count


walls = list(combinations(empty_pos, 3))

for wall in walls:
    for x, y in wall:
        lab[x][y] = 1
    #print(lab)
    #바이러스 퍼뜨리기
    answer = max(answer, bfs(lab, virus_pos))
    for x, y in wall:
        lab[x][y] = 0
print(answer)