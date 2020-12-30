import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
Map = []
red = []
blue = []
visited = [[0]*100 for _ in range(100)]
answer = 11

for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'R':
            red = (i, j)
            tmp[j] = '.'
        elif tmp[j] == 'B':
            blue = (i, j)
            tmp[j] = '.'
    Map.append(tmp)

def in_bound(x, y):
    if x in range(0, n) and y in range(0, m):
        return True
    else:
        return False

#방향 i로 기울이기
def move(r_pos, b_pos, i):
    red_x, red_y = r_pos
    blue_x, blue_y = b_pos
    r_out, b_out = False, False
    r_cnt, b_cnt = 0, 0

    nx, ny = red_x+dx[i], red_y+dy[i]
    r_cnt += 1
    while in_bound(nx, ny):
        #벽을 만나면
        if Map[nx][ny] == '#':
            r_pos = (nx-dx[i], ny-dy[i])
            r_cnt -= 1
            break
        #구멍에 빠지면
        elif Map[nx][ny] == 'O':
            r_pos = (nx, ny)
            r_out = 1
            break
        else:
            red_x, red_y = nx, ny
            nx, ny = nx+dx[i], ny+dy[i]
            r_cnt += 1

    nx, ny = blue_x+dx[i], blue_y+dy[i]
    b_cnt += 1
    while in_bound(nx, ny):
        # 벽을 만나면
        if Map[nx][ny] == '#':
            b_pos = (nx - dx[i], ny - dy[i])
            b_cnt -= 1
            break
        # 구멍에 빠지면
        elif Map[nx][ny] == 'O':
            b_pos = (nx, ny)
            b_out = True
            break
        else:
            blue_x, blue_y = nx, ny
            nx, ny = nx + dx[i], ny + dy[i]
            b_cnt += 1

    #둘다 구멍에 빠지면
    if r_out == b_out == True:
        return r_pos, b_pos

    #같은 위치에 있으면
    if r_pos == b_pos:
        if r_cnt < b_cnt:
            b_pos = (b_pos[0]-dx[i], b_pos[1]-dy[i])
        else:
            r_pos = (r_pos[0]-dx[i], r_pos[1]-dy[i])

    return r_pos, b_pos


def bfs(red_pos, blue_pos):
    queue = deque([[red_pos, blue_pos, 0]])

    while queue:
        #print(queue)
        red_pos, blue_pos, count = queue.popleft()
        if count > 10:
            continue
        if Map[blue_pos[0]][blue_pos[1]] == 'O':
            continue
        if Map[red_pos[0]][red_pos[1]] == 'O':
            print(count)
            return
        else:
            for i in range(4):
                r_pos, b_pos = move(red_pos, blue_pos, i)
                if r_pos == red_pos and b_pos == blue_pos:
                    continue
                queue.append([r_pos, b_pos, count+1])
    print(-1)
bfs(red, blue)