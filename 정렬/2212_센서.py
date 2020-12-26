import sys

input = sys.stdin.readline
sensor = int(input())
base = int(input())
coord = list(map(int, input().split()))
coord.sort()

#기지국의 개수가 센서의 크기와 같거나 크면 -> 센서의 위치에 그냥 설치
if sensor <= base:
    print(0)
    sys.exit()

dist = []

#각 인접 센서 사이의 거리
for i in range(1, sensor):
    dist.append(coord[i]-coord[i-1])
dist.sort(reverse=True)

#k개의 구간으로 나누기 -> 가장 큰 원소부터 k-1개 제거
for i in range(base-1):
    dist.pop(0)

print(sum(dist))