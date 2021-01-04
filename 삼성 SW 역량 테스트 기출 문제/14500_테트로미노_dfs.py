import sys

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

def get_score(blocks):
    total = 0
    for block in blocks:
        total += board[block[0]][block[1]]
    return total

#(x,y)를 시작으로 4칸 찾기 -> ㅗ모양은 포함 못함 ㅠ
def dfs(x, y, block, count, max_num):
    global answer
    if count == 4:
        answer = max(answer, max_num)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_range(nx, ny) and (nx, ny) not in block:
            dfs(nx, ny, block+[(nx, ny)], count+1, max_num+board[nx][ny])

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
        dfs(i, j, [(i,j)], 1, board[i][j])
        #+모양도 추가하기
        exception(i, j)
        
            
print(answer)