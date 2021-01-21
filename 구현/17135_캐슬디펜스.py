import sys
import copy
from itertools import combinations

N, M, D = map(int, input().split())
board = []
answer = 0
enemies = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            enemies.append([i,j])
    board.append(tmp)

num = [i for i in range(M)]
#가능한 궁수 배치 경우
archers = list(combinations(num, 3))

for arc1, arc2, arc3 in archers:
    cur_enemies = copy.deepcopy(enemies, key = lambda x : (-x[0], x[1]))
    count = 0
    while True:
        #1. 공격하기
        D1, D2, D3 = N+M, N+M, N+M
        enemy1, enemy2, enemy3 = [0,0], [0,0], [0,0]
        #공격할 적 찾기
        for enemy in cur_enemies:
            #현재 체크하는 적 위치~각 궁수 위치까지의 거리
            d1 = abs(N-enemy[0]) + abs(arc1-enemy[1])
            d2 = abs(N-enemy[0]) + abs(arc2-enemy[1])
            d3 = abs(N-enemy[0]) + abs(arc3-enemy[1])

            if D1 > d1 and d1 <= D:
                #현재까지의 최소 거리이면
                D1 = d1
                enemy1 = enemy
            elif D1 == d1 and d1 <= D:
                if enemy1[1] > enemy[1]:
                    D1 = d1
                    enemy1 = enemy
            if D2 > d2 and d2 <= D:
                #현재까지의 최소 거리이면
                D2 = d2
                enemy2 = enemy
            elif D2 == d2 and d2 <= D:
                if enemy2[1] > enemy[1]:
                    D2 = d2
                    enemy2 = enemy
            if D3 > d3 and d3 <= D:
                #현재까지의 최소 거리이면
                D3 = d3
                enemy3 = enemy
            elif D3 == d3 and d3 <= D:
                if enemy3[1] > enemy[1]:
                    D3 = d3
                    enemy3 = enemy
        
        #찾은 적에 대해서 공격
        shot = set()
        if enemy1 != [0,0]:
            shot.add((enemy1[0], enemy1[1]))
            if enemy1 in cur_enemies:
                cur_enemies.remove(enemy1)
        if enemy2 != [0,0]:
            shot.add((enemy2[0], enemy2[1]))
            if enemy2 in cur_enemies:
                cur_enemies.remove(enemy2)
        if enemy3 != [0,0]:
            shot.add((enemy3[0], enemy3[1]))
            if enemy3 in cur_enemies:
                cur_enemies.remove(enemy3)
        count += len(shot)
        #2. 이동시키기
        i = 0
        while cur_enemies:
            if i >= len(cur_enemies):
                break
            cur_enemies[i][0] += 1
            #성에 도달하면
            if cur_enemies[i][0] >= N:
                cur_enemies.remove(cur_enemies[i])
            else:
                i+=1
        #3. 보드에 남은 적 있는지 확인
        if not cur_enemies:
            answer = max(answer, count)
            break

        
print(answer)