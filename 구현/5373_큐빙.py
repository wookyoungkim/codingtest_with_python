import sys
from collections import deque

input = sys.stdin.readline

color = {0:'w', 1:'y', 2:'r', 3:'o', 4:'g', 5:'b'}
rotation_target = {
    0:[3,4,2,5], # 뒤왼앞오
    3:[0,5,1,4], # 위오아왼
    1:[3,5,2,4], # 뒤오앞왼
    2:[0,4,1,5], # 위왼아오
    4:[0,3,1,2], # 위뒤밑앞
    5:[0,2,1,3] # 위앞밑뒤
}
rotation_idx = {
        0: [2,1,0,2,1,0,2,1,0,2,1,0], 
        1: [6,7,8,6,7,8,6,7,8,6,7,8], 
        2: [8,7,6,2,5,8,8,7,6,6,3,0], 
        3: [0,1,2,2,5,8,0,1,2,6,3,0],
        4: [6,3,0,2,5,8,2,5,8,6,3,0],
        5: [2,5,8,2,5,8,6,3,0,6,3,0]
}
side_num = {'U':0, 'D':1, 'F':2, 'B':3, 'L':4, 'R':5}

def rotate(side, direction):
    rotation_list = rotation_target[side] # 돌릴 면들
    lst = deque()
    
    for r in range(len(rotation_list)):
        for i in range(r*3, r*3+3):
            lst.append(cube[rotation_list[r]][rotation_idx[side][i]])

    if direction == '-':
        # 시계방향으로 3번
        for _ in range(3):
            m = lst.pop()
            lst.appendleft(m)
    else:
        # 시계방향으로 3번
        for _ in range(3):
            m = lst.popleft()
            lst.append(m)

    # 다시 맞게 넣어주기 
    for r in range(len(rotation_list)):
        for i in range(r*3, r*3+3):
            cube[rotation_list[r]][rotation_idx[side][i]] = lst.popleft()
    
    # 기준면도 회전
    tmp = []
    for i in range(0, len(cube[side]), 3):
        tmp.append(cube[side][i:i+3])
    n = len(tmp)
    m = len(tmp[0])
    result = [[0]* n for _ in range(m)]
    if direction == '+':
        # 시계방향으로
        for i in range(n):
            for j in range(m):
                result[j][n-i-1] = tmp[i][j]
    else:
        # 반시계방향으로
        for i in range(n):
            for j in range(m):
                result[n-1-j][i] = tmp[i][j]

    for i in range(n):
        for j in range(m):
            cube[side][3*i+j] = result[i][j]

N = int(input())
for _ in range(N):
    cube = [
    [0 for _ in range(9)], [1 for _ in range(9)], 
    [2 for _ in range(9)], [3 for _ in range(9)], 
    [4 for _ in range(9)], [5 for _ in range(9)]
    ]

    n = int(input().strip()) # 큐브 n번 회전
    rotations = input().split()
    
    for r in rotations:
        rotate(side_num[r[0]], r[1])
    c = 0
    for _ in range(3):
        for i in range(c, c+3):
            print(color[cube[0][i]], end='')
        c += 3
        print()
