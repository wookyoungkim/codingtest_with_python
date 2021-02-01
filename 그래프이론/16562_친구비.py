import sys
sys.setrecursionlimit(10 ** 9)

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if money[a] < money[b]:
        parent[b] = a
    else:
        parent[a] = b

N, M, k = map(int, input().split())
money = [0] + list(map(int, input().split()))
parent = [0] * (N + 1) 
for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
print(parent)
grouped_parent = sorted(list(enumerate(parent)), key= lambda x:x[1])
print(grouped_parent)
answer = 0
n = 1
tmp = []

for i in range(1, len(grouped_parent)):
    if grouped_parent[i][1] == n:
        tmp.append(money[grouped_parent[i][0]])
    else:
        answer += min(tmp)
        tmp = [money[grouped_parent[i][0]]]
        n += 1
    
answer += min(tmp)
if answer > k:
    print("Oh no")
else:
    print(answer)