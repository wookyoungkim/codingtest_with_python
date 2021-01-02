import sys

input = sys.stdin.readline

N = int(input())
sconductor = list(map(int, input().split()))
visited = [0]*(N+1)
diff = []
for i in range(N):
    diff.append([abs(i-sconductor[i]+1), i+1, sconductor[i]])
diff = sorted(diff, key= lambda x: x[0])
print(diff)

answer = 0
for i in range(len(diff)):
    print(diff[i])
    if diff[i][1] > diff[i][2]:
        start, end = diff[i][2], diff[i][1]
    else:
        start, end = diff[i][1], diff[i][2]
        
    if 1 not in visited[start:end+1]:
        answer += 1
        for j in range(start, end+1):
            visited[j] = 1
    else:
        break
    print(visited)
print(answer)