import sys

input = sys.stdin.readline

def in_range(x,y):
    if x in range(n) and y in range(m):
        return True
    return False

def get_max_gold(n, m, gold):
    result = 0

    #m회 이동만큼
    for j in range(1, m):
        # i번째 열의 행 확인하기
        for i in range(n):
            #세 방향의 범위 확인하기
            #왼쪽위
            if in_range(i+1, j-1):
                left_up = gold[i+1][j-1]
            else:
                left_up = 0
            #왼쪽
            left = gold[i][j-1]
            #왼쪽아래
            if in_range(i-1, j-1):
                left_down = gold[i-1][j-1]
            else:
                left_down = 0
            gold[i][j] += max(left_up, left, left_down)
    for i in range(n):
        result = max(result, gold[i][m-1])
    return result

tc = int(input())
answer = []

for i in range(tc):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    
    gold = []
    idx = 0
    for j in range(n):
        gold.append(tmp[idx:idx+m])
        idx += m
    answer.append(get_max_gold(n, m, gold))
print(answer)