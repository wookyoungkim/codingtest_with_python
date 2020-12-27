import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
limit = list(map(int, input().strip().split()))
limit.sort(reverse=True)

M = int(input())
weight = list(map(int, input().strip().split()))
weight.sort(reverse=True)

answer = 0

if limit[0] < weight[0]:
    print(-1)
    sys.exit()

#모든 크레인에 대해 해당 크레인이 옮길 수 있는 가장 큰 상자 찾기
while weight:
    for l in limit:
        for j in range(len(weight)):
            if l >= weight[j]:
                weight.pop(j)
                break
    answer += 1
print(answer)