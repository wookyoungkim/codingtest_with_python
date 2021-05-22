import sys
from collections import deque
import heapq

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def in_bound(x, y):
    if x in range(N) and y in range(M):
        return True
    return False

M, N = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, list(input().strip()))))

queue = []
heapq.heappush(queue, [0,0,0])
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = 0

while queue:
    count, x, y = heapq.heappop(queue)

    if x == N-1 and y == M-1:
        print(count)
        break

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_bound(nx, ny) and visited[nx][ny] == False:
            if board[nx][ny] == 1:
                heapq.heappush(queue, [count+1, nx,ny])
            else:
                heapq.heappush(queue, [count, nx,ny])
            visited[nx][ny] = True
            
