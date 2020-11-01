import sys
import copy
from collections import deque
import itertools
input = sys.stdin.readline

answer = 0
n, m = map(int, input().split())
lab = []
empty = []

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        if l[j] == 0:
            empty.append([i,j])
    lab.append(l)

def check(lab):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                queue.append([i,j])
    #print(queue)
    while queue:
        i,j = queue.popleft()
        if i-1>=0 and lab[i-1][j] == 0:
            lab[i-1][j] = 2
            queue.append([i-1, j])
        if i+1<n and lab[i+1][j] == 0:
            lab[i+1][j] = 2
            queue.append([i+1, j])
        if j-1>=0 and lab[i][j-1] == 0:
            lab[i][j-1] = 2
            queue.append([i, j-1])
        if j+1<m and lab[i][j+1] == 0:
            lab[i][j+1] = 2
            queue.append([i, j+1])
    #print(lab)

def solution():
    wall = list(itertools.combinations(empty, 3))
    global answer
    for w in wall:
        viruslab = copy.deepcopy(lab)
        count = 0
        for i in range(3):
            viruslab[w[i][0]][w[i][1]] = 1
        #print(lab)
        check(viruslab)
        for i in range(len(viruslab)):
            count += viruslab[i].count(0)
        answer = max(answer, count)
        for i in range(3):
            viruslab[w[i][0]][w[i][1]] = 0

solution()
print(answer)
