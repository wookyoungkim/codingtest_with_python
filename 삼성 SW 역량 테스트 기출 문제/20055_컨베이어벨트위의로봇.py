import sys

input = sys.stdin.readline

N, K = map(int, input().split())
durability = list(map(int, input().split()))
robots = [0 for _ in range(N)]
robot_count = 1
count = 0
answer = 1

def rotate(l, n):
    return l[-n:] + l[:-n]

while True:
    # 1번 과정
    durability = rotate(durability, 1)
    robots = rotate(robots, 1)
    if robots[N-1] != 0:
        # 로봇 내리기
        robots[N-1] = 0
    
    # 2번 과정
    for i in range(N-2, -1, -1):
        if robots[i] != 0 and robots[i+1] == 0 and durability[i+1] >= 1:
            # 빈칸이고 내구성 1 이상이면
            robots[i+1] = robots[i]
            robots[i] = 0
            durability[i+1] -= 1
            if durability[i+1] == 0:
                count += 1
    if robots[N-1] != 0:
        # 로봇 내리기
        robots[N-1] = 0
    
    # 3번 과정
    if durability[0] != 0:
        robots[0] = robot_count
        robot_count += 1
        durability[0] -= 1
        if durability[0] == 0:
                count += 1
    
    if count >= K:
        print(answer)
        break
    else:
        answer += 1

