import sys
import math

input = sys.stdin.readline

N = int(input())
board = [[0]*101 for _ in range(101)]
curves = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    curves.append(list(map(int, input().split())))

def rotate(pre, x, y, n):
    # 기준점 x, y 기준으로 curve의 모든 좌표 회전시키기
    new_g = []
    max_x, max_y = 0, 0
    max_len = 0
    rotation = []
    for i in range(n):
        rotation += dp[i]

    for a,b in rotation:
        if (a, b) != (x, y):
            d_x, d_y = x-a, y-b
            n_x, n_y = x+d_y, y-d_x
            new_g.append((n_x, n_y))
            if (a, b) == (c[0], c[1]):
                end[n] = [n_x, n_y]
    return new_g

def dragon_curve(n):
    if dp[n]:
        return dp[n]
    else:
        # dp로 드래곤커브 좌표 구하기
        dp[n] = rotate(dragon_curve(n-1), end[n-1][0], end[n-1][1], n)

for c in curves:
    # dp[i] : 시작좌표 (x,y)기준 번째 세대
    dp = [[] for _ in range(20)]
    end = [[] for _ in range(20)]

    dp[0] = [(c[0], c[1]), (c[0]+dx[c[2]], c[1]+dy[c[2]])]
    end[0] = [c[0]+dx[c[2]], c[1]+dy[c[2]]]
    dragon_curve(c[3]) #n번째까지 드래곤커브의 좌표 구하기

    for i in range(len(dp)):
        if not dp[i]:
            break
        else:
            # 드래곤 커브 표시하기
            for d in dp[i]:
                board[d[1]][d[0]] = 1
                
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j+1] == 1 and board[i+1][j] == 1 and board[i+1][j+1] == 1:
            answer += 1

print(answer)