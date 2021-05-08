from itertools import combinations
from collections import defaultdict, deque

def find(tree, n, visited, num):
    queue = deque()
    queue.append(n)
    visited[n] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += num[node]
        for t in tree[node]:
            if visited[t] == False:
                visited[t] = True
                queue.append(t)
    return count

def solution(k, num, links):
    answer = float('inf')
    
    link = []
    for i in range(len(links)):
        if links[i][0] != -1:
            link.append([i, links[i][0]])
        if links[i][1] != -1:
            link.append([i, links[i][1]])
    
    possible = combinations(link, len(link)-k+1)
    for pos in possible:
        max_student = 0
        tree = defaultdict(list)
        for p in pos:
            tree[p[0]].append(p[1])
            tree[p[1]].append(p[0])

        visited = [False for _ in range(len(num))]
        for n in range(len(num)):
            if not visited[n]:
                max_student = max(max_student, find(tree, n, visited, num))
        answer = min(max_student, answer)

    return answer

print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))