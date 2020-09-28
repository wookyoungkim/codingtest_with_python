#왕실의 나이트

def solution():
    pos = list(input())
    pos[1] = int(pos[1])
    pos[0] = int(ord(pos[0]) - 96)
    count = 0

    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    for i in range(len(dx)):
        if 0 < pos[0]+dx[i] < 9 and 0 < pos[1]+dy[i] < 9:
            count += 1
    return count

print(solution())
