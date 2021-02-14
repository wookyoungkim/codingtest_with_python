import heapq

INF = int(1e9)

def dijkstra(start, distance, graph):
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

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)] #노드 연결 정보
    distance = [INF]*(n+1) #최단 거리 테이블

    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    dijkstra(s, distance, graph)
    #경우1) 각자 택시 따로 타기
    answer = distance[a] + distance[b]
    #경우2) 특정 지점까지 같이 타고 이후 각자 집까지
    for i in range(n+1):
        cost = 0
        distance_a = [INF]*(n+1)
        distance_b = [INF]*(n+1)
        if i != s:
            cost += distance[i]
            dijkstra(i, distance_a, graph)
            cost = cost + distance_a[a] + distance_a[b]
            answer = min(answer, cost)
    return answer

print(solution(6,	4,	5,	6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))