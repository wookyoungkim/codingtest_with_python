import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
Map = []
red = []
blue = []
visited = [[0]*100 for _ in range(100)]
answer = 11

for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'R':
            red = (i,j)
            tmp[j] = '.'
        elif tmp[j] == 'B':
            blue = (i,j)
            tmp[j] = '.'
    Map.append(tmp)

def bfs():
    queue = set([red, blue, 0])


