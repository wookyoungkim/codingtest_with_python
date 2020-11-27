import collections, copy

def solution(tickets):
	
    # 그래프 만들기
    graph = collections.defaultdict(list)

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
	
    # 출발점이 무조건 'ICN'
    queue = collections.deque([('ICN', ['ICN'])])
    result = []
	
    def find_path(graph, queue):
        n, path = queue.popleft()
		
        # 재귀 종료조건
        if len(path) == len(tickets)+1:
            result.append(path) # 완성된 경로 추가
            return

        for m in graph[n]:
            next_graph = copy.deepcopy(graph) # 그래프 깊은 복사
            queue.append((m, path + [m])) # 경로 분기
            next_graph[n].remove(m) # 방문한 공항 삭제
            find_path(next_graph,queue) # 재귀

    find_path(graph,queue)       
    result.sort() # 알파벳순 정렬
    return result[0]