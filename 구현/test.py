import copy

def in_bound(x, y,n):
    if x in range(n) and y in range(n):
        return True
    return False
    
def attack(i, j, p, r, maps):
    cur_maps = copy.deepcopy(maps)
    r1 = [(i-r//2, j-1),(i-r//2, j)]
    r2 = [(i-1, j+r//2-1), (i, j+r//2-1)]
    r3 = [(i+r//2-1, j-1),(i+r//2-1, j)]
    r4 = [(i-1, j-r//2), (i, j-r//2)]
    total = 0
    
    # 4가지의 경계에 대해서
    # r1~r2
    x, y = r1[1]
    while in_bound(x,y,len(maps)) and x in range(r1[1][0], r2[0][0]+1) and y in range(r1[1][1], r2[0][1]+1):
        if cur_maps[x][y] <= p/2:
            total += 1
        cur_maps[x][y] = -1
        x += 1
        y += 1
    
    # # r2~r3
    x, y = r2[1]
    while in_bound(x,y,len(maps)) and x in range(r2[1][0], r3[1][0]+1) and y in range(r3[1][1], r2[1][1]+1):
        if cur_maps[x][y] <= p/2:
            total += 1
        cur_maps[x][y] = -1
        x += 1
        y -= 1
    
    # r3~r4
    x, y = r3[0]
    while in_bound(x,y,len(maps)) and x in range(r4[1][0], r3[0][0]+1) and y in range(r4[1][1], r3[0][1]+1):
        if cur_maps[x][y] <= p/2:
            total += 1
        cur_maps[x][y] = -1
        x -= 1
        y -= 1
    
    # r4~r1
    x, y = r4[0]
    while in_bound(x,y,len(maps)) and x in range(r1[0][0], r4[0][0]+1) and y in range(r4[0][1], r1[0][1]+1):
        if cur_maps[x][y] <= p/2:
            total += 1
        cur_maps[x][y] = -1
        x -= 1
        y += 1
    
    print(total)
    for x in range(len(maps)):
        y = 0
        while y < len(maps):
            if cur_maps[x][y] == -1:
                y += 1
                while in_bound(x,y,len(maps)) and cur_maps[x][y] != -1:
                    if cur_maps[x][y] <= p:
                        total += 1
                    cur_maps[x][y] = -1
                    y += 1
                y+= 1
            else:
                y += 1
    return total
    
def solution(maps, p, r):
    answer = 0
    n = len(maps)
    for i in range(n):
        for j in range(n):
            answer = max(answer, attack(i,j,p,r,maps))
    return answer

print(solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],	19,	6))