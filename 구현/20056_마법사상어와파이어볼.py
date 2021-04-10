import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fireball = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fireball(x, y, m, s, d):
    # d방향으로 s만큼 이동시키기 (m, s, d)
    nx, ny = (x+dx[d]*s)%N, (y+dy[d]*s)%N
    return nx, ny

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([r-1, c-1, m, s, d])
    fireball.append([r-1, c-1, m, s, d])

for move in range(K):
    # 1. 모든 파이어볼에 대해서 방향 d로 s만큼 이동하기 
    for f in range(len(fireball)):
        r, c, m, s, d = fireball[f]
        nx, ny = move_fireball(r, c, m, s, d)
        board[nx][ny].append([nx, ny, m, s, d])
        board[r][c].remove([r, c, m, s, d])

    # 2. 이동 후 한칸에 2개이상 존재하는지
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1: 
                length = len(board[i][j])
                # 2개 이상이면
                sumM, sumS, oddcount, evencount = 0, 0, 0, 0
                for f in board[i][j]:
                    sumM += f[2]
                    sumS += f[3]
                    if f[4] % 2 == 0:
                        evencount += 1
                    else:
                        oddcount += 1
                # 나눈 뒤 질량이 0보다 크면 4개로 나누기
                if sumM // 5 != 0:
                    m, s = sumM//5, sumS//length
                    if oddcount == 0 or evencount == 0:
                        # 전부 홀수거나 짝수면
                        board[i][j] = [[i,j,m,s,0], [i,j,m,s,2], [i,j,m,s,4], [i,j,m,s,6]]
                    else:
                        board[i][j] = [[i,j,m,s,1], [i,j,m,s,3], [i,j,m,s,5], [i,j,m,s,7]]
                # 아니면 전체 소멸
                else:
                    board[i][j] = []

    # 3. fireball 정보 갱신
    fireball = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                fireball += board[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        for f in board[i][j]:
            answer += f[2]

print(answer)