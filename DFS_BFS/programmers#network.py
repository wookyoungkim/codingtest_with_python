visited = [False] * 200
answer = 0

def dfs(idx, computers):
    global answer
    #해당 노드가 방문하지 않으면
    #print(idx+1, visited[idx])
    if visited[idx] == False:
        visited[idx] = True
        answer += 1
    for i in range(len(computers[idx])):
        if idx != i and computers[idx][i] == 1:
            if visited[i] == False:
                visited[i] = True
                dfs(i, computers)
    
def solution(n, computers):
    for i in range(len(computers)):
        dfs(i, computers)
    return answer

print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))