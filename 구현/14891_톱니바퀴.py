import sys

input = sys.stdin.readline

def anticlockwise(sawtooth):
    zero = sawtooth[0]
    for i in range(len(sawtooth)-1):
        sawtooth[i] = sawtooth[i+1]
    sawtooth[-1] = zero
    #print(sawtooth)

def clockwise(sawtooth):
    zero = sawtooth[-1]
    for i in range(len(sawtooth)-1, 0, -1):
        sawtooth[i] = sawtooth[i-1]
    sawtooth[0] = zero
    #print(sawtooth)

def solution():
    sawtooth = [[]]
    for i in range(4):
        sawtooth.append(list(map(int, list(input().strip()))))
    K = int(input())
    rotations = []
    for i in range(K):
        rotations.append(list(map(int, input().split())))
    
    for num, dir in rotations:
        rotate = {-1:[], 1:[]}
        rotate[dir].append(num)
        # 1. 왼쪽도 돌려야 하는지 확인
        if num-1 >= 1 and sawtooth[num][6] != sawtooth[num-1][2]:
            rotate[-1 * dir].append(num-1)
            if num-2 >= 1 and sawtooth[num-1][6] != sawtooth[num-2][2]:
                rotate[dir].append(num-2)
                if num-3 >= 1 and sawtooth[num-2][6] != sawtooth[num-3][2]:
                    rotate[-1 * dir].append(num-3)

        # 2. 오른쪽도 돌려야 하는지 확인
        if num+1 <= 4 and sawtooth[num][2] != sawtooth[num+1][6]:
            rotate[-1 * dir].append(num+1)
            if num+2 <= 4 and sawtooth[num+1][2] != sawtooth[num+2][6]:
                rotate[dir].append(num+2)
                if num+3 <= 4 and sawtooth[num+2][2] != sawtooth[num+3][6]:
                    rotate[-1 * dir].append(num+3)

        # 3. 회전
        for r in rotate[1]:
                clockwise(sawtooth[r])
        for r in rotate[-1]:
            anticlockwise(sawtooth[r])

    result = 0

    for i in range(len(sawtooth)-1):
        if sawtooth[i+1][0] == 1:
            result += 2**i
    return result


print(solution())