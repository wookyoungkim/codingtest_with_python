#볼링공 고르기
from itertools import combinations
import math

def nCr(n, r):
    return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

def solution():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    num = []
    ans = len(list(combinations(data, 2)))

    for weight in range(1, M+1):
        num.append(int(data.count(weight)))
    for n in num:
        if n != 1 and n != 0:
            ans -= nCr(n, 2)
    print(ans)
    return ans


solution()

