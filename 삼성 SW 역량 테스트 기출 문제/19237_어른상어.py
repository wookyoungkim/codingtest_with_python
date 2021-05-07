import sys
from collections import deque, defaultdict

input = sys.stdin.readline

dx = [0, -1, 1, 0, 0] # 상1하2좌3우4
dy = [0, 0, 0, -1, 1]

N, M, K = map(int, input().split())
n_shark = M
def in_range(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

smell = [[0 for _ in range(N)] for _ in range(N)] # smell[i][j] = [상어번호, 남은시간]
shark = [[[] for _ in range(N)] for _ in range(N)] # shark[i][j] = [k] : (i,j)에 현재 k번 상어있음 -> 한칸에 여러 상어 있는지 검사용
sharks = {} # shark[k] = [d, (x,y)] : k번 상어가 d 방향 보고 (x,y)에 위치
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] != 0:
            shark[i][j].append(tmp[j])
            sharks[tmp[j]] = [(i,j)]
            smell[i][j] = [tmp[j], K] #초기 냄새, 시간 퍼뜨리기

direction = list(map(int, input().split()))
for i in range(M):
    sharks[i+1].append(direction[i])

priority = defaultdict(list) # priority[k][d] : k번 상어의 방향 d 우선순위
for i in range(M):
    for j in range(4):
        # i번 상어의 각 네방향 마다의 우선순위
        priority[i+1].append(list(map(int, input().split())))

time = 0
# 매초마다의 동작
while True:
    if n_shark == 1:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break
    
    # 모든 상어 이동
    for s in sharks.keys():
        (x, y), d = sharks[s]
        count_empty = [] # 빈칸 count
        count_me = [] # 내 냄새가 있는 칸
        # 4방향 검사하기
        for i in range(1, 5):
            nx, ny = x+dx[i], y+dy[i]
            if in_range(nx, ny):
                # 빈칸 count
                if smell[nx][ny] == 0:
                    count_empty.append(i)
                # 내 냄새가 있는 칸인지 count
                elif smell[nx][ny][0] == s:
                    count_me.append(i)
        
        if len(count_empty) == 1:
            # 해당 칸으로 이동하기
            shark[x][y].remove(s)
            shark[x+dx[count_empty[0]]][y+dy[count_empty[0]]].append(s)
            sharks[s] = [(x+dx[count_empty[0]],y+dy[count_empty[0]]), count_empty[0]]
        elif len(count_empty) > 1:
            # 우선순위에 따라 이동하기 -> priority[k][d] : k번 상어의 d번 priority에 따라
            for p in priority[s][d-1]:
                if p in count_empty:
                    # 해당 방향으로 이동
                    shark[x][y].remove(s)
                    shark[x+dx[p]][y+dy[p]].append(s)
                    sharks[s] = [(x+dx[p],y+dy[p]), p]
                    break

        elif len(count_me) == 1:
            # 해당 칸으로 이동하기
            shark[x][y].remove(s)
            shark[x+dx[count_me[0]]][y+dy[count_me[0]]].append(s)
            sharks[s] = [(x+dx[count_me[0]],y+dy[count_me[0]]), count_me[0]]
        elif len(count_me) > 1:
            # 우선순위에 따라 이동하기 -> priority[k][d] : k번 상어의 d번 priority에 따라
            for p in priority[s][d-1]:
                if p in count_me:
                    # 해당 방향으로 이동
                    shark[x][y].remove(s)
                    shark[x+dx[p]][y+dy[p]].append(s)
                    sharks[s] = [(x+dx[p],y+dy[p]), p]
                    break
    
    # 한칸에 여러 상어 있는지?
    for i in range(N):
        for j in range(N):
            if len(shark[i][j]) > 1:
                shark[i][j].sort()
                # 제일 번호 작은 상어 빼고 다 내보내기
                del_shark = shark[i][j][1:]
                for s in del_shark:
                    (x, y), d = sharks[s]
                    shark[x][y].remove(s)
                    del(sharks[s])
                    n_shark -= 1

    # 남은시간 -= 1
    for i in range(N):
        for j in range(N):
            if smell[i][j] != 0:
                if smell[i][j][1] == 1:
                    smell[i][j] = 0
                else:
                    smell[i][j][1] -= 1

    # 냄새 뿌리기
    for s in sharks.keys():
        (x, y), d = sharks[s]
        smell[x][y] = [s, K]
    
    time += 1