import collections, copy

def solution(tickets):
    graph = collections.defaultdict(list)

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
	
    # 출발점이 무조건 'ICN'
    queue = collections.deque([('ICN', ['ICN'])])
    result = []
	
    def find_path(graph, queue):
        n, path = queue.popleft()

        if len(path) == len(tickets)+1:
            result.append(path)
            return

        for m in graph[n]:
            next_graph = copy.deepcopy(graph)
            queue.append((m, path + [m]))
            next_graph[n].remove(m)
            find_path(next_graph,queue)

    find_path(graph,queue)       
    result.sort()
    return result[0]