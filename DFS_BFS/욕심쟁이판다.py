import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_bound(x, y):
    if x in range(0, N) and y in range(0, N):
        return True
    else:
        return False

def dfs(x, y):
    #이미 계산한 좌표면 더 계산할 필요 없이 바로 리턴
    if visited[x][y]:
        return visited[x][y]
    #방문하지 않은 좌표의 기본값은 1
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_bound(nx, ny):
            if Map[nx][ny] > Map[x][y]:
                #현재까지 계산한 최대 살 수 있는 날과 해당 좌표부터 계산한 값+현재 좌표값 비교
                visited[x][y] = max(visited[x][y], dfs(nx, ny)+1)
    return visited[x][y]
    
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
#각 지점을 포함하여 앞으로 며칠 더 살 수 있는지 계산
visited = [[0]*N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i,j))
print(answer)