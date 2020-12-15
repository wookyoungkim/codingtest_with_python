import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    x = int(input())
    houses.append(x)
houses.sort()

# 이분탐색의 대상 : 가장 인접한 두 공유기 사이의 거리
start = houses[1] - houses[0]
end = houses[-1] - houses[0]

while start <= end:
    #현재 가장 인접한 두 공유기 사이의 거리 찾기
    gap = (start + end) // 2
    value = houses[0]
    count = 0

    #실제로 공유기 배치하기
    for house in houses:
        #설치가능하면
        if house >= value + gap:
            value = house
            count += 1

    #C개 이상의 공유기 설치할 수 없으면 거리 감소
    if count < C:
        end = gap - 1
    #C개 이상의 공유기 설치 가능
    else:
        start = gap + 1
        result = gap
print(result)