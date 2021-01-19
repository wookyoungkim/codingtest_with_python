import sys

input = sys.stdin.readline

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

n, m = map(int, input().split())
parents = [i for i in range(n+1)]
roads = []
result = 0
last = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    roads.append([cost, a, b])
roads.sort()

for road in roads:
    if find(parents, road[1]) != find(parents, road[2]):
        union(road[1], road[2])
        result += road[0]
        last = road[0]
print(result-last)