import sys
from collections import defaultdict
input = sys.stdin.readline

dice = list(map(int, input().split()))
# board[i]:[(score, next)] -> i번째 칸은 (score 점수, 다음 칸)
board = defaultdict()
for i in range(21):
    board[i] = [(i*2, i+1)]
board[21] = [(0, -1)] # 도착칸

board[5].append((10, 22))
board[22] = [(13, 23)]
board[23] = [(16, 24)]
board[24] = [(19, 25)]

board[10].append((20, 29)) 
board[29] = [(22, 30)]
board[30] = [(24, 25)]

board[15].append((30, 28))
board[28] = [(28, 27)]
board[27] = [(27, 26)]
board[26] = [(26, 25)]

board[25] = [(25, 31)]
board[31] = [(30, 32)]
board[32] = [(35, 20)]

horses = [0 for _ in range(4)]
answer = 0

def move(moves, h):
    # h번째말 moves번 이동시키기
    x = horses[h]
    next_pos = 0
    flag = False
    
    # 처음 1칸 이동
    if x in [5,10,15]:
        next_pos = board[x][1][1]
    else:
        next_pos = board[x][0][1]
    
    # 이동한 칸이 도착칸이면
    if next_pos == 21:
        horses[h] = next_pos
        flag = True
    else:
        # moves-1칸 이동
        for i in range(moves-1):
            next_pos = board[next_pos][0][1]
            if next_pos == 21:
                # 이동하다가 도착칸을 만나면
                horses[h] = next_pos
                flag = True
                break
    
    # 현재 말의 상태 갱신 -> 도착한 칸에 다른 말 있는지 검사
    if flag != True:
        for i in range(len(horses)):
            if i != h:
                if horses[i] == next_pos:
                    return -1
        horses[h] = next_pos
                    
    return board[horses[h]][0][0]

def dfs(dice, score):
    global answer
    if len(dice) == 0:
        # 주사위 10번에 대해서 다 돌았으면
        answer = max(answer, score)
        return
    
    for h in range(4):
        if horses[h] != 21:
            x = horses[h]
            # 해당 말 dice[0]만큼 이동 후 얻은 점수 계산
            score_this_turn = move(dice[0], h)
            if score_this_turn < 0:
                continue
            dfs(dice[1:], score+score_this_turn)
            # 이전 상태로 돌리기
            horses[h] = x

dfs(dice, 0)
print(answer)