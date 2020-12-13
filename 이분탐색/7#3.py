import sys
input = sys.stdin.readline

N,C = map(int, input().split())
houses = []
routers = []
for _ in range(N):
    x = int(input())
    houses.append(x)
houses.sort()

#gap의 크기를 이분탐색하기
start = houses[1] - houses[0]
end = houses[-1] - houses[0]
result = 0

while start <= end:
    #가장 인접한 두 공유기 사이의 거리
    mid = (start + end)//2
    value = houses[0]
    count = 1

    #현재 mid값을 이용한 공유기 설치
    for i in range(1, N):
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1
    #c개 이상의 공유기를 설치할 수 있는 경우 -> 거리 증가
    if count >= C:
        start = mid + 1
        result = mid
    #c개 이상의 공유기를 설치할 수 있는 경우 -> 거리 감소
    else:
        end = mid - 1

print(result)