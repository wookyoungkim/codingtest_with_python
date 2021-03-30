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
        if dir == 1:
            #clockwise
            clo, anti = [num], []
            # 1. 왼쪽도 돌려야 하는지 확인
            if num-1 >= 1 and sawtooth[num][6] != sawtooth[num-1][2]:
                anti.append(num-1)
                if num-2 >= 1 and sawtooth[num-1][6] != sawtooth[num-2][2]:
                    clo.append(num-2)
                    if num-3 >= 1 and sawtooth[num-2][6] != sawtooth[num-3][2]:
                        anti.append(num-3)
    
            # 2. 오른쪽도 돌려야 하는지 확인
            if num+1 <= 4 and sawtooth[num][2] != sawtooth[num+1][6]:
                anti.append(num+1)
                if num+2 <= 4 and sawtooth[num+1][2] != sawtooth[num+2][6]:
                    clo.append(num+2)
                    if num+3 <= 4 and sawtooth[num+2][2] != sawtooth[num+3][6]:
                        anti.append(num+3)

            # 3. 회전
            for c in clo:
                    clockwise(sawtooth[c])
            for a in anti:
                anticlockwise(sawtooth[a])
            
        else:
            clo, anti = [], [num]
            # 1. 왼쪽도 돌려야 하는지 확인
            if num-1 >= 1 and sawtooth[num][6] != sawtooth[num-1][2]:
                clo.append(num-1)
                if num-2 >= 1 and sawtooth[num-1][6] != sawtooth[num-2][2]:
                    anti.append(num-2)
                    if num-3 >= 1 and sawtooth[num-2][6] != sawtooth[num-3][2]:
                        clo.append(num-3)
    
            # 2. 오른쪽도 돌려야 하는지 확인
            if num+1 <= 4 and sawtooth[num][2] != sawtooth[num+1][6]:
                clo.append(num+1)
                if num+2 <= 4 and sawtooth[num+1][2] != sawtooth[num+2][6]:
                    anti.append(num+2)
                    if num+3 <= 4 and sawtooth[num+2][2] != sawtooth[num+3][6]:
                        clo.append(num+3)

            # 3. 회전
            for c in clo:
                    clockwise(sawtooth[c])
            for a in anti:
                anticlockwise(sawtooth[a])
    result = 0

    for i in range(len(sawtooth)-1):
        if sawtooth[i+1][0] == 1:
            result += 2**i
    return result


print(solution())