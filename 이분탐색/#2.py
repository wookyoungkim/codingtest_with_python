#이분탐색말고도 계수정렬이나 집합 사용가능
import sys

input = sys.stdin.readline

def binary_search(parts, key):
    start = 0
    end = len(parts)-1

    while start <= end:
        mid = (start+end)//2
        if parts[mid] == key:
            return key
        elif parts[mid] > key:
            start = mid+1
        else:
            end = mid-1
    return -1

N = int(input())
parts = sorted(list(map(int, input().split())))
M = int(input())
requested_parts = sorted(list(map(int, input().split())))
answer = ""

for part in requested_parts:
    if binary_search(parts, part) == -1:
        answer = "No"
print("Yes") if answer != "No" else print(answer)
