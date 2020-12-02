import sys
input = sys.stdin.readline

def find_first(start, end, list, key):
    while start <= end:
        mid = (start+end)//2
        print(start, end, mid)
        if list[mid] == key:
            if list[mid-1] != key:
                return mid
            else:
                end = mid-1
        elif list[mid] > key:
            end = mid-1
        else:
            start = mid+1
    return -1

def find_last(start, end, list, key):
    while start <= end:
        mid = (start+end)//2
        print(start, end, mid)
        if list[mid] == key:
            if list[mid+1] != key:
                return mid
            else:
                start = mid+1
        elif list[mid] > key:
            end = mid-1
        else:
            start = mid+1
    return -1

N, x = map(int, input().split())
nums = list(map(int, input().split()))
first_idx = find_first(0, len(nums)-1, nums, x) if find_first(0, len(nums)-1, nums, x)!=-1 else 0
last_idx = find_last(0, len(nums)-1, nums, x) if find_last(0, len(nums)-1, nums, x)!=-1 else 0

if last_idx == 0 and first_idx == 0: 
    print(0)
else:
    print(last_idx - first_idx + 1)
    