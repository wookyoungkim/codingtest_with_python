import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def in_range(x, y):
    if x in range(N) and y in range(M):
        return True
    return False
    
def bfs(x,y):
    max_num = 0
    queue = deque()
    #x, y, 이전 x, 이전 y, count, total_score
    queue.append((x, y, 0, 0, 1, board[x][y]))

    while queue:
        x, y, pre_x, pre_y, cnt, total_score = queue.popleft()
        if cnt == 4:
            max_num = max(max_num, total_score)
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            #이동한 좌표가 행렬의 범위를 만족하고, 해당 이동이 이전 좌표로의 이동이 아니면 !!
            if in_range(nx, ny) and (nx, ny) != (pre_x, pre_y):
                queue.append((nx, ny, x, y, cnt+1, total_score+board[nx][ny]))
    return max_num

def get_score(blocks):
    total = 0
    for block in blocks:
        total += board[block[0]][block[1]]
    return total

def exception(x, y):
    global answer
    tmp = []
    min_val = 1000
    for i in range(4):
        if in_range(x+dx[i], y+dy[i]):
            min_val = min(min_val, board[x+dx[i]][y+dy[i]])
            tmp.append((x+dx[i], y+dy[i]))
    # 범위 내에 ㅗ모양이 가능하면
    if len(tmp) == 3:
        tmp.append((x,y))
        answer = max(answer, get_score(tmp))
    #범위 내에 +모양이 가능하면 -> 네방향중 제일 작은 칸 빼서 ㅗ로 만들기
    elif len(tmp) == 4:
        tmp.append((x,y))
        answer = max(answer, get_score(tmp)-min_val)

for i in range(N):
    for j in range(M):
        answer = max(answer, bfs(i,j))
        #+모양도 추가하기
        exception(i, j)
            
print(answer)