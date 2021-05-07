import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
answer = float('inf')

def seperate(x, y, d1, d2):
    seperated = [[0 for _ in range(N)] for _ in range(N)]
    population = [0 for _ in range(5)]

    # 5번 선거구
    for i in range(d1+1):
        seperated[x+i][y-i] = 5
        seperated[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        seperated[x+i][y+i] = 5
        seperated[x+d1+i][y-d1+i] = 5
    for i in range(N):
        for j in range(N):
            if seperated[i][j] == 5:
                k = j+1
                while k<N and seperated[i][k] != 5:
                    k+= 1
                if k<N:
                    # j~k까지 5로
                    for l in range(j+1, k):
                        seperated[i][l] = 5
                    break
    
    # 1번 선거구
    for i in range(x+d1):
        for j in range(y+1):
            if seperated[i][j] != 5:
                seperated[i][j] = 1
    # 2번 선거구
    for i in range(x+d2+1):
        for j in range(y+1, N):
            if seperated[i][j] != 5:
                seperated[i][j] = 2
    # 3번 선거구
    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if seperated[i][j] != 5:
                seperated[i][j] = 3
    # 4번 선거구
    for i in range(x+d2+1, N):
        for j in range(y-d1+d2, N):
            if seperated[i][j] != 5:
                seperated[i][j] = 4
    
    for i in range(N):
        for j in range(N):
            population[seperated[i][j]-1] += board[i][j]
    return max(population) - min(population)

for x in range(N):
    for y in range(N):
        # 가능한 모든 d1, d2 찾기
        for d1 in range(1, y+1):
            for d2 in range(1, N-y):
                if d1+d2 <= N-x-1:
                    answer = min(answer, seperate(x, y, d1, d2))

print(answer)

