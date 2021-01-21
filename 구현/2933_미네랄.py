import sys
from collections import deque
import copy

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C = map(int, input().split())
cave = []
for _ in range(R):
    cave.append(list(input().strip()))
N = int(input())
attacks = list(map(int, input().split()))
for i in range(len(attacks)):
    attacks[i] = R - attacks[i]

def print_cave(cave):
    for i in range(len(cave)):
        for j in range(len(cave[0])):
            print(cave[i][j], end='')
        print()

def in_range(x, y):
    if x in range(R) and y in range(C):
        return True
    else:
        return False

def attack_mineral(i):
    if i % 2 == 0:
        #왼쪽에서부터 공격
        j = 0
        while j < C :
            if cave[attacks[i]][j] == 'x':
                break
            j += 1
    else:
        #오른쪽에서부터 공격
        j = C-1
        while j >= 0:
            if cave[attacks[i]][j] == 'x':
                break
            j -= 1
    return j

def get_mineral(x, y):
    queue = deque([(x, y)])
    visited = [[-1]*C for _ in range(R)]
    visited[x][y] = 1
    cluster = [[x, y]]

    while queue:
        x, y = queue.popleft()
        #클러스터 찾기
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx == R:
                #벽에 닿아있으면 -> 아래로 떨어뜨릴 필요 x
                return []
            if in_range(nx, ny) and cave[nx][ny] == 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cluster.append([nx, ny])
    return cluster

def move_mineral(cluster, cave):
    cluster = sorted(cluster, key = lambda x : (-x[0], -x[1]))
    #한칸씩 내리기
    while True:
        ccluster = copy.deepcopy(cluster)
        ccave = copy.deepcopy(cave)
        for c in ccluster:
            if c[0]+1 == R or ccave[c[0]+1][c[1]] == 'x':
                #다른 미네랄과 닿거나 바닥에 닿으면,
                return cluster, cave
            else:
                ccave[c[0]][c[1]] = '.'
                ccave[c[0]+1][c[1]] = 'x'
                c[0] += 1
        else:
            cluster = ccluster
            cave = ccave



for i in range(N):
    #미네랄 부시기
    j = attack_mineral(i)
    if j in range(C):
        if cave[attacks[i]][j] == 'x':
            cave[attacks[i]][j] = '.'
        #공중에 떠있는 미네랄 검사
        for k in range(4):
            nx, ny = attacks[i]+dx[k], j+dy[k]
            if in_range(nx, ny) and cave[nx][ny] == 'x':
                cluster = get_mineral(nx, ny)
                if cluster:
                    cluster, cave = move_mineral(cluster, cave)
                    break
        
print_cave(cave)

