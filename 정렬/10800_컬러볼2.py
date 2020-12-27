N = int(input())

sum_weight = 0
balls = [] 
color = [0] * (N+1)
ans = [0] * N

for i in range(N):
    balls.append([i] + list(map(int, input().split())))
# 크기 기준 오름차순 정렬
balls = sorted(balls,key=lambda l:l[2])

j = 0
for i in range(N):
    while balls[i][2] > balls[j][2]:
        sum_weight += balls[j][2]
        color[balls[j][1]] += balls[j][2]
        j += 1
	# 해당 공의 정답은 누적합에서 현재 자신의 색깔 누적합 값을 빼면 된다
    ans[balls[i][0]] = (sum_weight - color[balls[i][1]])

for x in ans:
    print(x)