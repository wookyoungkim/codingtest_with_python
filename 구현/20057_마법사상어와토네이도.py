import sys
import math

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 입력받기
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
answer = 0 # 격자 밖으로 나간 모래 양

# 범위내인지 판단
def in_bound(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

# 이동시키기
def move(x, y, d):
    sand = A[x][y]
    degree = [0, 270, 180, 90]
    dis = [(0,-2), (-1,-1), (-1,0), (-1,1), (-2,0), (1,-1), (1,0), (1,1), (2,0)]
    
    this_dis = []
    # 이번 방향에 대한 이동 좌표 구하기
    for di in dis:
        rad = degree[d] * (math.pi / 180.0)
        ny = round(math.cos(rad)*di[1] - math.sin(rad)*di[0])
        nx = round(math.sin(rad)*di[1] + math.cos(rad)*di[0])
        this_dis.append((nx,ny))
    move_sand = [0.05, 0.1, 0.07, 0.01, 0.02, 0.1, 0.07, 0.01, 0.02]
    moved = 0
    global answer
    #9칸에 대해서 이동
    for i in range(9):
        nx, ny = x+this_dis[i][0], y+this_dis[i][1]
        moving_sand = int(sand*move_sand[i]) # 현재 움직일 모래의 양
        moved += moving_sand
        if in_bound(nx, ny):
            A[nx][ny] += moving_sand
        else:
            # 격자 밖으로 나간 모래 count
            answer += int(sand*move_sand[i])
    # a칸에 대해서 이동
    ax, ay = x+dx[d], y+dy[d]
    left = sand - moved
    if in_bound(ax, ay):
        A[ax][ay] += left
    else:
        answer += left
    # x,y 칸의 모래 계산
    A[x][y] = 0

x, y, d = N//2, N//2, 0
count = 0 # moves만큼 2번 이동했는지?
cur_moves = 0 # 현재 이 방향으로 몇번 이동했는지?
moves = 1 # 이 방향으로 몇칸 이동해야 하는지?

while True:
    if cur_moves == moves:
        cur_moves = 0
        count += 1
        d = (d+1)%4
    if count == 2:
        count = 0
        moves += 1
    
    # 중심 1칸 이동하기
    x, y = x+dx[d], y+dy[d]
    # 모래 이동하기
    move(x, y, d)

    if (x,y) == (0,0):
        # (0,0)까지 이동 완료했으면
        break
    cur_moves += 1

print(answer)