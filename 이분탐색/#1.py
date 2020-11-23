N = int(input())
parts = list(map(int, input().split()))
parts.sort()
M = int(input())
customers = list(map(int, input().split()))
flag = 0

def binary_search(array, target):
    start = 0
    end = len(array)-1
    mid = (start + end) // 2

    while start <= end:
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return False

for c in customers:
    if binary_search(parts, c) is False:
        flag = -1

if flag == -1:
    print("No")
else:
    print("Yes")