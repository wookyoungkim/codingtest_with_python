import sys
from collections import defaultdict

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def in_bound(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

N = int(input())
students = defaultdict()
for _ in range(N**2):
    num, s1, s2, s3, s4 = map(int, input().split())
    students[num] = [s1,s2,s3,s4]

board = [[0 for _ in range(N)] for _ in range(N)]

# 1. 자리 정하기
for s in students.keys():
    # 모든 학생에 대해서
    cur_max = [-1, -1, -1, -1] # likes, empty, x, y
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                # 빈칸이면
                likes, empty = 0, 0
                for k in range(4):
                    ni, nj = i+dx[k], j+dy[k]
                    if in_bound(ni,nj):
                        if board[ni][nj] in students[s]:
                            likes += 1
                        elif board[ni][nj] == 0:
                            empty += 1
                if likes > cur_max[0]:
                    cur_max = [likes, empty, i, j]
                elif likes == cur_max[0] and empty > cur_max[1]:
                    cur_max = [likes, empty, i, j]
    board[cur_max[2]][cur_max[3]] = s

# 2. 만족도 구하기
answer = 0
for i in range(N):
    for j in range(N):
        count = 0
        num = board[i][j]
        for k in range(4):
            ni, nj = i+dx[k], j+dy[k]
            if in_bound(ni,nj):
                if board[ni][nj] in students[num]:
                    count += 1
        if count != 0:
            answer += 10**(count-1)

print(answer)