#치킨 배달
import itertools

def get_chicken_distance(house, chicken):
    return abs(house[0]-chicken[0])+abs(house[1]-chicken[1])

def solution():
    N, M = map(int, input().split())
    chickens = []
    house = []

    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            if tmp[j] == 2:
                chickens.append([i, j])
            elif tmp[j] == 1:
                house.append([i,j])
    min_total = (N+N) * len(house)
    
    #살릴 치킨집 M개 고르기
    possible = list(itertools.combinations(chickens, M))
    
    for pos in possible:
        total = 0
        for h in house:
            min_dis = N + N
            for c in pos:
                cur = get_chicken_distance(h, c)
                if cur < min_dis:
                    min_dis = cur
            total += min_dis
        if total < min_total:
            min_total = total

    return min_total

print(solution())