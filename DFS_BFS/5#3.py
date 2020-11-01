import sys
import heapq
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, k = map(int, input().split())
path = []
virus = []
time = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] != 0:
            heapq.heappush(virus, [0, tmp[j], i, j])
    path.append(tmp)

S, X, Y = map(int, input().split())
while virus:
    time, virusNum, x, y = heapq.heappop(virus)
    if time >= S:
        break
    #상하좌우 증식
    for k in range(4):
        if 0<=x+dx[k]<n and 0<=y+dy[k]<n:
            if path[x+dx[k]][y+dy[k]] == 0:
                path[x+dx[k]][y+dy[k]] = virusNum
                heapq.heappush(virus, [time+1, virusNum, x+dx[k], y+dy[k]])
    #print(virus)   
print(path[X-1][Y-1])
