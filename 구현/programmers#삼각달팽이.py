#다음 좌표 구하기
def get_next(cur_y, cur_x, cur_d):
    DIR = {'U': (-1, -1), 'D': (1, 0), 'R': (0, 1)}
    dy, dx = DIR[cur_d][0], DIR[cur_d][1]
    nxt_y, nxt_x = cur_y + dy, cur_x + dx
    return nxt_y, nxt_x

#회전해야하는지 체크
def check_turn(nxt_y, nxt_x, n, snail):
    #범위(0~N)을 벗어났거나 이미 숫자가 채워진 경우 방향 바꿈
    return nxt_y < 0 or nxt_y >= n or nxt_x > nxt_y or snail[nxt_y][nxt_x] != 0

def solution(n):
    answer = []
    #다음방향
    NEXT = {'U': 'D', 'D': 'R', 'R': 'U'}
    N = sum(range(1, n+1))
    snail = [[0] * i for i in range(1, n+1)]

    #초기 좌표와 방향
    cur_y, cur_x, cur_d = 0, 0, 'D'
    for num in range(1, N+1):
        snail[cur_y][cur_x] = num
        next_x, next_y = get_next(cur_y, cur_x, cur_d)
        if check_turn(next_x, next_y, n, snail):
            cur_d = NEXT[cur_d]
        cur_y, cur_x = get_next(cur_y, cur_x, cur_d)

    for i in snail:
        answer += i
    return answer

print(solution(5))