import sys
from collections import defaultdict, deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M, left = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
taxi_x, taxi_y = map(int, input().split())
taxi = [taxi_x-1, taxi_y-1]

passengers = defaultdict()
for i in range(2, M+2):
    s_x, s_y, e_x, e_y = list(map(int, input().split()))
    passengers[i] = [s_x-1, s_y-1, e_x-1, e_y-1]
    board[passengers[i][0]][passengers[i][1]] = i

def in_bound(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

def find_passenger(taxi):
    queue = deque()
    queue.append([taxi[0], taxi[1], 0])
    visited = [[False for _ in range(N)] for _ in range(N)]
    possible = []

    while queue:
        x, y, c = queue.popleft()
        if board[x][y] > 1:
            # 승객이 있으면
            possible.append([c, board[x][y], x, y])
            #return c, board[x][y]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_bound(nx, ny) and board[nx][ny] != 1 and visited[nx][ny] == False:
                # 범위 안이고 빈칸이면
                queue.append([nx, ny, c+1])
                visited[nx][ny] = True
    if possible:
        return sorted(possible, key = lambda x:[x[0], x[2], x[3]])[0][:2]
    else:
        return -1, -1

def drive(passenger):
    start_x, start_y, end_x, end_y = passenger
    queue = deque([[start_x, start_y, 0]])
    visited = [[False for _ in range(N)] for _ in range(N)]

    while queue:
        x, y, c = queue.popleft()
        if x == end_x and y == end_y:
            # 목적지 도달
            return c
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if in_bound(nx, ny) and board[nx][ny] != 1 and visited[nx][ny] == False:
                # 범위 안이고 빈칸이면
                queue.append([nx, ny, c+1])
                visited[nx][ny] = True
    return -1

while passengers:
    # 1. 승객 고르기
    moves, i = find_passenger(taxi)

    # 2. 택시~승객까지 이동하기
    if left < moves or moves == -1:
        print(-1)
        sys.exit(0)
    start_x, start_y, end_x, end_y = passengers[i]
    taxi = [start_x, start_y]
    board[start_x][start_y] = 0
    left -= moves

    # 3. 출발지~도착지까지 이동
    moves = drive(passengers[i])
    if left < moves or moves == -1:
        print(-1)
        sys.exit(0)
    taxi = [end_x, end_y]
    left += moves # 연료 2배로 충전
    del(passengers[i])

print(left)