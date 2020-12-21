import sys
from itertools import combinations
from bisect import bisect_left

input = sys.stdin.readline
N = int(input())
solution = list(map(int, input().split()))
solution.sort()

#두개의 용액을 뽑는다
two_sol = list(combinations(solution, 2))
min_val = float('inf')
answer = [solution[0], solution[1], solution[2]]

for sol in two_sol:
    total = sum(sol)
    last = solution[bisect_left(solution, -total)-1]
    if abs(min_val) > abs(total + last):
        min_val = total
        answer = [sol[0], sol[1], last]
answer.sort()
for ans in answer:
    print(ans, end=" ")