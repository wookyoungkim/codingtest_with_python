import sys

input = sys.stdin.readline

def binary_search(start, end, list, key):
    min_val = start
    while start <= end:
        mid = (start+end)//2
        sum = 0
        for l in list:
            if l-mid > 0: 
                sum += l-mid
        if sum >= key:
            min_val = min(mid, min_val)
            start = mid+1
        else:
            end = mid-1
    return min_val 

N, M = map(int, input().split())
rice_cake = sorted(list(map(int, input().split())))
print(binary_search(max(rice_cake)-M, max(rice_cake), rice_cake, M))

