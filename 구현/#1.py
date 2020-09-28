#상하좌우
def solution():
    N = int(input())
    path = list(input().split())
    pos = [1, 1]

    for p in path:
        if p == 'R':
            if pos[1] + 1 > N:
                continue
            else:
                pos[1] += 1
        elif p == 'L':
            if pos[1] - 1 < 1:
                continue
            else:
                pos[1] -= 1
        elif p == 'U':
            if pos[0] - 1 < 1:
                continue
            else:
                pos[0] -= 1
        else:
            if pos[0] + 1 > N:
                continue
            else:
                pos[0] += 1
    
    return pos

print(solution())
