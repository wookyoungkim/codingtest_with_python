import sys

input = sys.stdin.readline
N, H = map(int, input().split())

bottom = [] #석순 -> 길이 i 이상면 부셔야함
top = [] #종유석 -> 길이 N-i 이상이면 부셔야함
for _ in range(N//2):
    bottom.append(int(input().strip()))
    top.append(int(input().strip()))
bottom.sort()
top.sort()

#lst에서 x보다 큰 데이터의 개수 구하기
def binary_search(lst, x):
    start, end = 0, len(lst)-1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return len(lst) - (end+1)

answer = N
count = 0
for i in range(1, H+1):
    tmp = binary_search(bottom, i-1) + binary_search(top, H-i)
    if tmp < answer:
        answer = tmp
        count = 1
    elif tmp == answer:
        count += 1

print(answer, count)