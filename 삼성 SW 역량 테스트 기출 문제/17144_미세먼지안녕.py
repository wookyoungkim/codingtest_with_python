import sys

input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    if x in range(R) and y in range(C):
        return True
    return False

R, C, T = map(int, input().split())
room = []
aircleaner = []
for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j] == -1:
            # 공청기 위치 기록
            aircleaner.append((i,j))
    room.append(tmp)

for time in range(T):
    check_room = [[0 for _ in range(C)] for _ in range(R)]
    # 1. 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                # 미세먼지 있으면
                if room[i][j] >= 5:
                    count = 0
                    for d in range(4):
                        # 확산 가능한 네방향 체크
                        ni, nj = i+dx[d], j+dy[d]
                        if in_range(ni, nj) and room[ni][nj] != -1:
                            check_room[ni][nj] += room[i][j]//5
                            count += 1
                    room[i][j] -= (room[i][j]//5)*count
    for i in range(R):
        for j in range(C):
            room[i][j] += check_room[i][j]

    
    # 2. 공청기 가동
    for a in range(2):
        # 시계방향으로 확산시키기
        x, y, d = aircleaner[a][0]+dx[a], aircleaner[a][1], a
        while True:
            nx, ny = x+dx[d], y+dy[d]
            if (nx, ny) == aircleaner[a]:
                room[x][y] = 0
                break
            if a == 0:
                # 시계방향 확산일때
                if nx < 0:
                    nx, ny = x, y+1
                    d = 3
                elif nx > aircleaner[a][0]:
                    nx, ny = x, y-1
                    d = 2
                elif ny >= C:
                    nx, ny = x+1, y
                    d = 1
            elif a == 1:
                if nx >= R:
                    nx, ny = x, y+1
                    d = 3
                elif nx < aircleaner[a][0]:
                    nx, ny = x, y-1
                    d = 2
                elif ny >= C:
                    nx, ny = x-1, y
                    d = 0

            room[x][y] = room[nx][ny]
            x, y = nx, ny

answer = 0
for r in room:
    answer += sum(r)
print(answer + 2)