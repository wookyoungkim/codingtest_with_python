# 트리 문제는 이전에 풀어본 적이 없어서 문제를 딱 읽고 어떻게 풀어야될지 아예 감이 오지 않았다,,
# 정확성의 기준이 N=20이길래 빠르게 bfs로 정확성만 맞추고 3번의 효율성을 고민하러 갔다,,

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
    # 1. links의 입력대로 트리 저장하기 
    for i in range(len(links)):
        if links[i][0] != -1:
            link.append([i, links[i][0]])
        if links[i][1] != -1:
            link.append([i, links[i][1]])
    
    # 2. nCk-1로 전체 간선중에 살릴 간선 고르기
    possible = combinations(link, len(link)-k+1)
    for pos in possible:
        max_student = 0
        # 각 노드마다의 연결 관계를 표시
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