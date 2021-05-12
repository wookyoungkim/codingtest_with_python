import sys
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
words = []
alph = set()
readable = ['a', 'n', 't', 'i', 'c']

for _ in range(N):
    words.append(list(input().strip()))
    for w in words[-1][4:-4]:
        if w not in readable:
            alph.add(w)

if K < 5:
    print(0)
    sys.exit(0)

K -= 5
if len(alph) <= K:
    print(len(words))
    sys.exit(0)
else:
    pos = combinations(alph, K)

answer = 0
for p in pos:
    count = 0
    for word in words:
        flag = True
        for w in word[4:-4]:
            if w not in readable and w not in p:
                flag = False
                break
        if flag == True:
            count += 1
    answer = max(answer, count)

print(answer)