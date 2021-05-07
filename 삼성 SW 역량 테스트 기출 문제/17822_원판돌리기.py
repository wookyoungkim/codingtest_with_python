import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split()) #N개의 원판 위에 M개의 숫자, K번 회전
disk = []
rotations = []
for _ in range(N):
    disk.append(list(map(int, input().split())))

for _ in range(K):
    # 번호가 x인 원판 d 방향으로 k칸 회전
    rotations.append(list(map(int, input().split())))

def rotate(x, d, k):
    before = copy.deepcopy(disk[x])
    direction = 0
    if d == 0:
        direction = 1
    else:
        direction = -1

    for i in range(len(before)):
        ni = (i + direction * k) % M
        disk[x][ni] = before[i]

for x, d, k in rotations:
    # 1. 번호가 x의 배수인 원판을 d방향으로 k칸 회전시키기
    for i in range(N):
        if (i+1)%x == 0:
            rotate(i, d, k)

    # 2. 인접한 수 모두 찾기 
    total_adj = set()
    for i in range(N):
        for j in range(M):
            same_adj = [(i,j)]
            cur = disk[i][j]
            if disk[i][j] == 0:
                continue
            # 인접한 10방향 전부 확인
            else:
                if i in range(1, N-1):
                    if disk[i-1][j] == cur:
                        same_adj.append((i-1,j))
                    if disk[i+1][j] == cur:
                        same_adj.append((i+1,j))
                elif i == 0:
                    if disk[1][j] == cur:
                        same_adj.append((1,j))
                elif i == N-1:
                    if disk[N-2][j] == cur:
                        same_adj.append((N-2,j))
                if j in range(1, M-1):
                    if disk[i][j-1] == cur:
                        same_adj.append((i,j-1))
                    if disk[i][j+1] == cur:
                        same_adj.append((i,j+1))
                elif j == M-1:
                    if disk[i][M-2] == cur:
                        same_adj.append((i,M-2))
                    if disk[i][0] == cur:
                        same_adj.append((i,0))
                elif j == 0:
                    if disk[i][1] == cur:
                        same_adj.append((i,1))
                    if disk[i][M-1] == cur:
                        same_adj.append((i,M-1))
            if len(same_adj) > 1:
                for s in same_adj:
                    total_adj.add(s)
    # 인접하고 같은 수가 있으면 지우기
    if total_adj:
        for t in total_adj:
            disk[t[0]][t[1]] = 0

    # 이번 회전에서 지워진게 없으면
    else:
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if disk[i][j] != 0:
                    total += disk[i][j]
                    cnt += 1
        if cnt != 0:
            avg = total/cnt
            for i in range(N):
                for j in range(M):
                    if disk[i][j] != 0:
                        if avg < disk[i][j]:
                            disk[i][j] -= 1
                        elif avg > disk[i][j]:
                            disk[i][j] += 1
        else:
            break

answer = 0
for i in range(N):
    answer += sum(disk[i])

print(answer)

