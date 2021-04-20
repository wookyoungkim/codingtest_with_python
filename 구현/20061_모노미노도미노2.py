import sys

input = sys.stdin.readline

dx = [0, 1] # 파란칸으로, 초록칸으로
dy = [1, 0]
answer = 0

def in_bound(blocks):
    for b in blocks:
        if (b[0] in range(4) and b[1] in range(10)) or (b[0] in range(10) and b[1] in range(4)):
            continue
        else:
            return False
    return True

def get_blue(board):
    blue = []
    for i in range(len(board[:4])):
        blue.append(board[i][4:])
    return list(zip(*blue))

def get_green(board):
    green = []
    for i in range(len(board[4:])):
        green.append(board[i+4][:4])
    return green

def move(blocks, d):
    while True:
        new_blocks = []
        for b in blocks:
            new_blocks.append((b[0]+dx[d], b[1]+dy[d]))
        
        flag = False
        if in_bound(new_blocks):
            for b in new_blocks:
                if board[b[0]][b[1]] != 1:
                    flag = True
                elif (b[0], b[1]) in blocks:
                    flag = True
                else:
                    flag = False
                    break
        if flag:
            blocks = new_blocks
        else:
            # 움직이기 끝
            for b in blocks:
                board[b[0]][b[1]] = 1
            break

def check_push(check_board, d):
    global answer
    count = 0
    for i in range(len(check_board[2:])):
        if sum(check_board[i+2]) == 4:
            push(check_board, i+2) # i+idx번째까지 밀기
            count += 1
    
    if count > 0:
        answer += count
        if d == 0:
            # 다시 돌려서 대입
            check_board = list(zip(*check_board))
            for i in range(len(check_board)):
                board[i][4:] = check_board[i]
        else:
            # 그대로 대입
            for i in range(len(check_board)):
                board[i+4][:4] = check_board[i]

def push(board, n):
    for i in range(n, -1, -1):
        board[i] = board[i-1]
    board[0] = [0,0,0,0]

def check_special(check_board, d):
    count = 0
    for i in range(2):
        # 특별칸에 블록이 있으면
        if sum(check_board[i]) > 0:
            count += 1
    if count > 0:
        special_push(check_board, count) # 열 수만큼 밀기
        # 다시 돌려서 대입
        if d == 0:
            check_board = list(zip(*check_board))
            for i in range(len(check_board)):
                board[i][4:] = check_board[i]
        else:
            # 그대로 대입
            for i in range(len(check_board)):
                board[i+4][:4] = check_board[i]

def special_push(board, count):
    for _ in range(count):
        for i in range(len(board)-1 , -1, -1):
            board[i] = board[i-1]
        board[0] = [0,0,0,0]

N = int(input())
board = [[0 for _ in range(10)] for _ in range(10)]

for _ in range(N):
    t, x, y = map(int, input().split())
    blocks = [(x,y)]
    if t == 2:
        blocks.append((x,y+1))
    elif t == 3:
        blocks.append((x+1,y))

    # 1. 이동하기
    move(blocks, 0) # 파란 칸으로 이동
    move(blocks, 1) # 초록 칸으로 이동

    #  2. 행/열 꽉 찼는지 확인
    count = check_push(get_blue(board), 0)
    count = check_push(get_green(board), 1)

    # 3. 특별칸에 block있는지?
    check_special(get_blue(board), 0)
    check_special(get_green(board), 1)
    

left = 0
for b in board:
    left += sum(b)

print(answer)
print(left)