import sys
from itertools import combinations

input = sys.stdin.readline

L, C = input().split()
chars = sorted(list(input().split()))

vowels = ['a', 'e', 'i', 'o', 'u']
combination = combinations(chars, int(L))
answer = []

for com in combination:
    n_v, n_c = 0, 0
    for c in com:
        if c in vowels:
            n_v += 1
        else:
            n_c += 1
    if n_v >= 1 and n_c >= 2:
        answer.append(com)
        
answer.sort()
for a in answer:
    print(''.join(a))