import sys

input = sys.stdin.readline

r,c,k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
time = 0

def operationR(board):
    # board의 모든 행 정렬하기
    count = [{} for _ in range(len(board))] # board의 각 행 숫자 등장 횟수 count

    # 1. 등장 횟수 count
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                if board[i][j] in count[i].keys():
                    count[i][board[i][j]] += 1
                else:
                    count[i][board[i][j]] = 1
    
    # 2. dic을 value 기준 오름차순, key 기준 내림차순 정렬하기
    maxlen = 0
    for i in range(len(count)):
        sort = sorted(count[i].items(), key= lambda x:[x[1], x[0]])
        board[i] = []
        for s in sort:
            board[i] += list(s)
        if len(board[i]) > 100:
            board[i] = board[i][:100]
        maxlen = max(maxlen, len(board[i]))
    
    # 3. 최대값 기준으로 0 append 해주기 -> 길이 맞추려고 & 100개 넘어가면 버리기
    if len(board) > 100:
        board = board[:100]
    for b in board:
        if len(b) < maxlen:
            for i in range(maxlen-len(b)):
                b.append(0)
    
    return board

def operationC(board):
    # board의 모든 열 정렬하기
    new_board = []
    for b in list(zip(*board)):
        new_board.append(list(b))
    count = [{} for _ in range(len(new_board))] # board의 각 행 숫자 등장 횟수 count

    # 1. 등장 횟수 count
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] != 0:
                if new_board[i][j] in count[i].keys():
                    count[i][new_board[i][j]] += 1
                else:
                    count[i][new_board[i][j]] = 1
    
    # 2. dic을 value 기준 오름차순, key 기준 내림차순 정렬하기
    maxlen = 0
    for i in range(len(count)):
        sort = sorted(count[i].items(), key= lambda x:[x[1], x[0]])
        new_board[i] = []
        for s in sort:
            new_board[i] += list(s)
        if len(new_board[i]) > 100:
            new_board[i] = new_board[i][:100]
        maxlen = max(maxlen, len(new_board[i]))
    
    # 3. 최대값 기준으로 0 append 해주기 -> 길이 맞추려고
    if len(new_board) > 100:
        new_board = new_board[:100]
    for b in new_board:
        if len(b) < maxlen:
            for i in range(maxlen-len(b)):
                b.append(0)
    
    # 4. 얘를 다시 행렬 바꿔서 리턴
    board = []
    for b in list(zip(*new_board)):
        board.append(list(b))
    
    return board


while time <= 100:
    # A[r][c] == k면
    if len(A) >= r and len(A[0]) >= c and A[r-1][c-1] == k:
        break

    # R 연산할지 C 연산할지?
    if len(A) >= len(list(zip(*A))):
        A = operationR(A)
    else:
        A = operationC(A)
    
    time += 1

if time > 100:
    print(-1)
else:
    print(time)