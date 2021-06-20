def dijkstra(start, end, distance, graph):
    #시작 노드 처리
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        #현재 노드가 이미 처리된 적 있는 노드면,
        if distance[now] < dist:
            continue
        #아니면,
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))

def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n+1)] #노드 연결 정보
    distance = [float('INF')]*(n+1) #최단 거리 테이블

    for r in roads:
        graph[r[0]].append((r[1],r[2]))

    answer = dijkstra(start, end, distance, graph)
    return answer

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))