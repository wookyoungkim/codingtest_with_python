import sys

input = sys.stdin.readline
N = int(input())
balls = []
answer = [0]*N
same_colors = [0]*N

#[공번호, 색깔번호, 크기]
for i in range(N):
    balls.append([i] + list(map(int, input().split())))

#같은 색의 누적 값 구하기
balls.sort(key = lambda x: [x[1],x[2]])
count = 1
for i in range(1,N):
    if balls[i][1] == balls[i-1][1]:
        #같은 색 같은 크기의 공에 대해서
        if balls[i][2] == balls[i-1][2]:
            same_colors[balls[i][0]] = same_colors[balls[i-1][0]]
            count += 1
        else:
            same_colors[balls[i][0]] = same_colors[balls[i-1][0]] + balls[i-1][2]*count
            count = 1
    else:
        count = 1

#단순 누적 값 구하기 -> 크기가 같은 다른색 공
balls.sort(key = lambda x: x[2])
for i in range(1, N):
    #같은 크기의 공에 대해서
    if balls[i][2] == balls[i-1][2]:
        answer[balls[i][0]] = answer[balls[i-1][0]]
        count += 1
    else:
        answer[balls[i][0]] = answer[balls[i-1][0]] + balls[i-1][2] * count
        count = 1

for i in range(N):
    print(answer[i] - same_colors[i])
