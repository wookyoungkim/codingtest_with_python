import sys
input = sys.stdin.readline

#오븐의 깊이, 피자 반죽 개수
D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

#지금까지 나온 오븐의 지름 중 가장 작은 값으로 바꿔줌
# 소팅된 결과를 얻을 수 있음
for i in range(1, D):
    oven[i] = min(oven[i], oven[i-1])

count = 0
last_idx = D-1

#오븐의 맨 밑부터 탐색
for i in range(D-1, -1, -1):
    #모든 피자 넣으면
    if count >= len(pizza):
        print(last_idx+1)
        sys.exit(0)
    #피자의 지름보다 오븐의 지름이 크면 -> 넣을 수 있음
    if oven[i] >= pizza[count]:
        count += 1
        last_idx = i
print(0)