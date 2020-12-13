import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ans = -1
start = 0
end = len(nums)-1

while start<=end:
    mid = (start+end)//2
    if mid == nums[mid]:
        ans = mid
        break
    elif N < nums[mid]:
        end = mid -1
    else:
        start = mid + 1
print(ans)