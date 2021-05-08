from collections import defaultdict, deque

def bfs(n, start, end, roads, traps):
    queue = deque()
    queue.append([start, 0])

    while queue:
        cur, count = queue.popleft()
        if cur == end:
            return count
        elif cur in traps:
            # trap밟으면 길 바꾸기
            new_road = defaultdict(list)
            for key, value in roads.items():
                if key == cur:
                    for v in value:
                        new_road[v[0]].append([key, v[1]])
                else:
                    for v in value:
                        if v[0] == cur:
                            new_road[v[0]].append([key, v[1]])
                        else:
                            new_road[key].append([v[0], v[1]])
            roads = new_road
        for r in roads[cur]:
            queue.append([r[0], count+r[1]])
    return -1

def solution(n, start, end, roads, traps):
    road_dic = defaultdict()
    for r in roads:
        road_dic[r[0]] = [[r[1], r[2]]]
    
    answer = bfs(n, start, end, road_dic, traps)
    return answer

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))