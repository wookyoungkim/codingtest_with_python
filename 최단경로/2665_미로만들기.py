import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    if x in range(n) and y in range(n):
        return True
    return False

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().strip())))
visited = [[False]*(n) for _ in range(n)]

queue = []
visited[0][0] = True
heapq.heappush(queue, (0,0,0))
while queue:
    count, x, y = heapq.heappop(queue)
    if x == n-1 and y == n-1:
        print(count)
        break
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_range(nx, ny) and visited[nx][ny] == False:
            visited[nx][ny] = True
            if board[nx][ny] == 0:
                heapq.heappush(queue, (count+1, nx, ny))
            else:
                heapq.heappush(queue, (count, nx, ny))