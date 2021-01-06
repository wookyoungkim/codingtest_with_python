import sys

N = int(input())
T = [[-1]*N for _ in range(N)]
tri = []
for _ in range(N):
    tri.append(list(map(int, input().split())))
T[0][0] = tri[0][0]

def in_range(x,y):
    if x in range(0,N) and y in range(0,N):
        return True
    else:
        return False
#위에서부터 계산
for i in range(1, N):
    for j in range(i+1):
        if in_range(i-1, j):
            from_left = T[i-1][j]
        else:
            from_left = 0
        if in_range(i-1, j-1):
            from_right = T[i-1][j-1]
        else:
            from_right = 0
        T[i][j] = tri[i][j] + max(from_left, from_right)

answer = 0
for i in range(N):
    answer = max(answer, T[N-1][i])
#print(T)
print(answer)
