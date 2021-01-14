import sys
input = sys.stdin.readline
INF = int(1e9)

def bf():
    for i in range(n):
        #n번의 라운드 반복
        for now, next_node, cost in edges:
            if dist[next_node] > dist[now]+cost:
                dist[next_node] = dist[now]+cost
                if i == n-1:
                    return True
    return False

tc = int(input())
answer = []
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    flag = False
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, t*(-1)))

    dist = [INF]*(n+1)
    if bf():
        answer.append("YES")
    else:
        answer.append("NO")
for a in answer:
    print(a)