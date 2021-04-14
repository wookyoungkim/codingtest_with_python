import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
lab = []
virus = []
empty = 0
answer = float('inf')
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 0:
            # 빈칸이면
            empty += 1
        elif tmp[j] == 2:
            virus.append((i,j))
    lab.append(tmp)

def in_range(x, y):
    if x in range(N) and y in range(N):
        return True
    else:
        return False

def diffusion(board, virus):
    cur_virus = deque(virus)
    time = 0
    cur_empty = empty
    
    while cur_virus:
        if time > answer:
            return float('inf')
        if cur_empty == 0:
            return time

        length = len(cur_virus)
        for l in range(length):
            x, y = cur_virus.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if in_range(nx, ny):
                    if board[nx][ny] == 0:
                        # 빈칸이면
                        cur_empty -= 1
                        board[nx][ny] = 3
                        cur_virus.append((nx, ny))
                    elif board[nx][ny] == 2:
                        # 비활성 바이러스면
                        board[nx][ny] = 3
                        cur_virus.append((nx, ny))
        time += 1
    if cur_empty == 0:
        return time
    else:
        return float('inf')

pos = list(combinations(virus, M))
for p in pos:
    # 가능한 M개 뽑기 조합마다 
    for x,y in p:
        # virus 활성 상태로
        lab[x][y] = 3
    clab = copy.deepcopy(lab)
    answer = min(answer, diffusion(clab, p))
    for x,y in p:
        # virus 비활성 상태로
        lab[x][y] = 2
if answer < float('inf'):
    print(answer)
else:
    print(-1)