import sys
import copy

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
            red = [i,j]
            tmp[j] = '.'
        elif tmp[j] == 'B':
            blue = [i,j]
            tmp[j] = '.'
    Map.append(tmp)

def in_bound(x, y):
    if x in range(0, n) and y in range(0,m):
        return True
    else:
        return False

#현재 공 위치에서 dir방향으로 옮기기
def dfs(count, red_pos, blue_pos, dir):
    global answer
    red_x, red_y = red_pos
    blue_x, blue_y = blue_pos

    #10번 넘어가면
    if count > 10:
        return

    r_out, b_out = False, False
    r_cnt, b_cnt = 0, 0

    #빨간공 움직이기
    nx, ny = red_x+dx[dir], red_y+dy[dir]
    while in_bound(nx, ny):
        r_cnt += 1
        #벽이면 이동 전 좌표 리턴하기
        if Map[nx][ny] == '#':
            red_pos = (red_x, red_y)
            r_cnt -= 1
            break
        elif Map[nx][ny] == 'O':
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
            b_out = True
            break
        else:
            blue_x, blue_y = nx, ny
            nx, ny = blue_x + dx[dir], blue_y + dy[dir]

    #파란 공이 구멍으로 빠진 경우 -> 실패
    if b_out:
        return
    #빨간공이 구멍으로 빠진 경우 -> 성공
    if r_out:
        answer = min(answer, count)
        return

    #같은 위치에 있으면
    if red_pos == blue_pos:
        #빨간공이 더 앞에 있었으면
        if r_cnt < b_cnt:
            blue_pos = (blue_x-dx[dir], blue_y-dy[dir])
        else:
            red_pos = (red_x-dx[dir], red_y-dy[dir])
    
    #움직일 수 없는 경우 더 볼 필요 x
    if r_cnt == b_cnt == 0:
        return

    for i in range(4):
        dfs(count+1, red_pos, blue_pos, i)

for i in range(4):
    dfs(1, red, blue, i)

if answer == 11:
    print(-1)
else:
    print(answer)