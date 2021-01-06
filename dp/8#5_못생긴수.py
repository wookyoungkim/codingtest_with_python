import sys

input = sys.stdin.readline

N = int(input())
nums = [0]*N
nums[0] = 1

#2,3,5배를 위한 인덱스
i2, i3, i5 = 0, 0, 0

#처음의 곱셈 값
next2, next3, next5 = 2, 3, 5

for i in range(1,N):
    nums[i] = min(next2, next3, next5)
    # 못생긴 수에 2,3,5를 곱한 수도 못생긴 수임을 이용하기
    #print(nums, i2, i3, i5, next2, next3, next5)
    if nums[i] == next2:
        i2 += 1
        next2 = nums[i2] * 2
    if nums[i] == next3:
        i3 += 1
        next3 = nums[i3] * 3
    if nums[i] == next5:
        i5 += 1
        next5 = nums[i5] * 5

print(nums[N-1])