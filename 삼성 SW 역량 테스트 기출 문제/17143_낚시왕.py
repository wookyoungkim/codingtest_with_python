import sys
from collections import defaultdict

input = sys.stdin.readline
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

R,C,M = map(int, input().split())
board = [[[] for _ in range(C)] for _ in range(R)]
reverse = {1:2, 2:1, 3:4, 4:3}
shark = defaultdict()
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1].append((i, z)) # 상어번호와 크기 저장
    shark[i] = [(r-1,c-1),s,d,z]

def in_bound(x, y):
    if x in range(R) and y in range(C):
        return True
    return False

def move(sharknum):
    (x,y),s,d,z = shark[sharknum]
    board[x][y].remove((sharknum,z))

    for i in range(s):
        nx, ny = x+dx[d], y+dy[d]
        if in_bound(nx, ny):
            # 범위 안이면 한칸 이동
            x, y = nx, ny
        else:
            # 격자 벗어나면 방향 반대
            d = reverse[d]
            x, y = x+dx[d], y+dy[d]
    
    # 상어 위치 갱신
    shark[sharknum] = [(x,y),s,d,z]
    board[x][y].append((sharknum, z))


fisher = -1 # 낚시왕의 y좌표
answer = 0
for t in range(C): # 낚시왕이 오른쪽 끝까지 이동할때까지
    # 1. 낚시왕 이동하기
    fisher += 1

    # 2. 상어잡기
    for i in range(R):
        if len(board[i][fisher]) > 0:
            # 상어 있으면 잡기
            answer += board[i][fisher][0][1]
            del(shark[board[i][fisher][0][0]])
            board[i][fisher] = []
            break
    
    # 3. 상어 이동하기
    for s in shark.keys():
        move(s)
    
    # 4. 이동 후 한칸에 2마리 이상?
    for i in range(R):
        for j in range(C):
            if len(board[i][j]) > 1:
                # 가장 무거운 순으로 sort
                sorted_board = sorted(board[i][j], key= lambda x:x[1], reverse=True)
                for s in sorted_board[1:]:
                    del(shark[s[0]])
                board[i][j] = [sorted_board[0]]

print(answer)
