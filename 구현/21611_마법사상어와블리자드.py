import sys

input = sys.stdin.readline

dx = [0, -1, 1, 0, 0] #상하좌우
dy = [0, 0, 0, -1, 1]

d_x = [0, 1, 0, -1]
d_y = [-1, 0, 1, 0] #(n//2, n//2) -> (0,0)까지의 이동시에 사용

N, M = map(int, input().split())
board = []
magic = []
for _ in range(N):
    board.append(list(map(int, input().split())))
for _ in range(M):
    magic.append(list(map(int, input().split())))

x, y = N//2, N//2 #상어의 위치
board[x][y] = float('inf')
answer = [0, 0, 0, 0]

def move_marble(marbles):
    new_marbles = []
    for i in range(len(marbles)):
        if marbles[i] != 0:
            new_marbles.append(marbles[i])
    return new_marbles

def bomb_marbles(marbles):
    while True:
        # 구슬 폭발
        if len(marbles) == 0:
            break
        marble_no = marbles[0]
        del_idx = [0]
        flag = False
        for i in range(1, len(marbles)):
            if marbles[i] == marble_no:
                del_idx.append(i)
            else:
                if len(del_idx) >= 4:
                    answer[marble_no] += len(del_idx)
                    flag = True
                    for d in del_idx:
                        marbles[d] = 0
                marble_no = marbles[i]
                del_idx = [i]
        if len(del_idx) >= 4:
            flag = True
            answer[marble_no] += len(del_idx)
            for d in del_idx:
                marbles[d] = 0
        if flag == False:
            break
        marbles = move_marble(marbles)
    return marbles

def change_marbles(marbles):
    new_marbles = []
    marble_no = marbles[0]
    del_idx = [0]
    for i in range(1, len(marbles)):
        if marbles[i] == marble_no:
            del_idx.append(i)
        else:
            new_marbles.append(len(del_idx))
            new_marbles.append(marble_no)
            marble_no = marbles[i]
            del_idx = [i]
    
    new_marbles.append(len(del_idx))
    new_marbles.append(marble_no)
    return new_marbles


for d, s in magic:
    # 1. 마법 시전하기
    for i in range(1, s+1):
        # d방향으로 s만큼 얼음 깨기
        nx, ny = x+dx[d]*i, y+dy[d]*i
        board[nx][ny] = 0
    
    marbles = [] # 1번칸부터 저장
    cur_x, cur_y = x, y
    move = 1 # 현재 방향에서 몇칸 이동해야 하는지?
    count = 0 # move만큼 몇칸 이동했는지?
    move_count = 0 # 현재 방향에서 몇칸 이동했는지?
    direction = 0 # 이동 방향

    while (cur_x, cur_y) != (0,0):
        if move_count == move:
            # 이번 방향에서 move만큼 이동했으면
            direction = (direction+1)%4
            move_count = 0
            count += 1

        if count == 2:
            # move만큼 2번 이동했으면
            count = 0
            move += 1

        n_x, n_y = cur_x+d_x[direction], cur_y+d_y[direction]
        marbles.append(board[n_x][n_y])
        cur_x, cur_y = n_x, n_y
        move_count += 1

    # 2. 구슬 이동하기
    marbles = move_marble(marbles)
    
    # 3. 구슬 폭발
    marbles = bomb_marbles(marbles)
    if len(marbles) == 0:
        break
    
    # 4. 구슬 변화
    marbles = change_marbles(marbles)

    # 5. 다시 옮겨넣기
    cur_x, cur_y = x, y
    move = 1 # 현재 방향에서 몇칸 이동해야 하는지?
    count = 0 # move만큼 몇칸 이동했는지?
    move_count = 0 # 현재 방향에서 몇칸 이동했는지?
    direction = 0 # 이동 방향
    while (cur_x, cur_y) != (0,0):
        if move_count == move:
            # 이번 방향에서 move만큼 이동했으면
            direction = (direction+1)%4
            move_count = 0
            count += 1

        if count == 2:
            # move만큼 2번 이동했으면
            count = 0
            move += 1

        n_x, n_y = cur_x+d_x[direction], cur_y+d_y[direction]
        if marbles:
            board[n_x][n_y] = marbles.pop(0)
        else:
            board[n_x][n_y] = 0
        cur_x, cur_y = n_x, n_y
        move_count += 1

print(answer[1]+2*answer[2]+3*answer[3])