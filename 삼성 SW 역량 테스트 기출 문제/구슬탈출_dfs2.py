import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
Map = []
red = []
blue = []
answer = 11

for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'R':
            red = (i,j)
            tmp[j] = '.'
        elif tmp[j] == 'B':
            blue = (i,j)
            tmp[j] = '.'
    Map.append(tmp)

def in_bound(x, y):
    if x in range(0, n) and y in range(0,m):
        return True
    else:
        return False

def move(red_pos, blue_pos, dir):
    red_x, red_y = red_pos
    blue_x, blue_y = blue_pos
    r_cnt, b_cnt = 0, 0
    r_out, b_out = False, False

    nx, ny = red_x+dx[dir], red_y+dy[dir]
    while in_bound(nx, ny):
        r_cnt += 1
        #벽이면 이동 전 좌표 리턴하기
        if Map[nx][ny] == '#':
            red_pos = (red_x, red_y)
            r_cnt -= 1
            break
        elif Map[nx][ny] == 'O':
            red_pos = (nx, ny)
            r_out = True
            break
        else:
            red_x, red_y = nx, ny
            nx, ny = red_x + dx[dir], red_y + dy[dir]

    #파란공 움직이기
    nx, ny = blue_x+dx[dir], blue_y+dy[dir]
    while in_bound(nx, ny):
        b_cnt += 1
        #벽이면 이동 전 좌표 리턴하기
        if Map[nx][ny] == '#':
            blue_pos = (blue_x, blue_y)
            b_cnt -= 1
            break
        elif Map[nx][ny] == 'O':
            blue_pos = (nx, ny)
            b_out = True
            break
        else:
            blue_x, blue_y = nx, ny
            nx, ny = blue_x + dx[dir], blue_y + dy[dir]

    #둘다 빠져나왔으면 바로 리턴
    if r_out == b_out == True:
        return (red_pos, blue_pos)

    #같은 위치에 있으면
    if red_pos == blue_pos:
        #빨간공이 더 앞에 있었으면
        if r_cnt < b_cnt:
            blue_pos = (blue_x-dx[dir], blue_y-dy[dir])
        else:
            red_pos = (red_x-dx[dir], red_y-dy[dir])
    return (red_pos, blue_pos) 

def dfs(red_pos, blue_pos, count):
    global answer
    #10번 넘어가면
    if count > 10:
        return
    #파란공이 구멍으로 빠진 경우 -> 실패
    if Map[blue_pos[0]][blue_pos[1]] == 'O':
        return
    #빨간공이 구멍으로 빠진 경우 -> 성공
    if Map[red_pos[0]][red_pos[1]] == 'O':
        answer = min(answer, count)
        return

    for i in range(4):
        #기울이기
        r_pos, b_pos = move(red_pos, blue_pos, i)
        #안움직였으면
        if r_pos == red_pos and b_pos == blue_pos:
            continue
        dfs(r_pos, b_pos, count+1)

dfs(red, blue, 0)

if answer == 11:
    print(-1)
else:
    print(answer)