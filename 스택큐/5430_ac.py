import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
answer = []

for t in range(T):
    funcs = list(input().strip())
    N = int(input())
    nums = list(input().strip("[]\n").split(","))
    if nums[0] != '':
        nums = list(map(int, nums))
        nums = deque(nums)
    else:
        nums = []
    
    flag = True

    count_reverse = 1 # 1: 원상태 2: 한번 reverse된 상태

    for f in funcs:
        if f == 'R':
            count_reverse *= -1
        elif f == 'D':
            if len(nums) == 0:
                flag = False
                print("error")
                break
            elif count_reverse == 1:
                nums.popleft()
            else:
                nums.pop()
    
    if flag:
        print("[", end='')

        if len(nums) > 0:
            if count_reverse == 1:
                for i in range(len(nums)-1):
                    print(nums[i], end=',')
                print(nums[-1], end='')
            else:
                for i in range(len(nums)-1, 0, -1):
                    print(nums[i], end=',')
                print(nums[0], end='')
        print("]")