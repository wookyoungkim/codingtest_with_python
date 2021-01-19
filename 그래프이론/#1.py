#팀결성
import sys
input = sys.stdin.readline

def find_parents(parents, x):
    #루트노드를 찾을때까지
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union(a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)

    if a > b:
        #a가 b를 가리키게
        parents[a] = b
    else:
        parents[b] = a

n, m = map(int, input().split())
parents = [i for i in range(n+1)]
print(parents)
for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        #union
        union(a, b)
    else:
        if find_parents(parents, a) == find_parents(parents, b):
            print("YES")
        else:
            print("NO")