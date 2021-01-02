import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

M, N, L = map(int, input().split())
hunters = list(map(int, input().split()))
hunters.sort()
animals = []
for _ in range(N):
    animals.append(list(map(int, input().split())))
animals.sort()
answer = 0

for animal in animals:
    l_idx = bisect_left(hunters, animal[0])
    r_idx = bisect_right(hunters, animal[0])
    h = 0
    if l_idx != r_idx:
        h = hunters[l_idx]
    else:
        if l_idx == 0:
            h = hunters[l_idx]
        elif r_idx == M:
            h = hunters[r_idx-1]
        elif abs(hunters[l_idx-1]-animal[0]) < abs(hunters[l_idx]-animal[0]):
            h = hunters[l_idx-1]
        else:
            h = hunters[r_idx]
    if abs(h-animal[0])+animal[1] <= L:
        answer += 1 
    
print(answer)