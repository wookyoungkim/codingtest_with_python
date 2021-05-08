from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def in_bound(x, y):
    if x in range(5) and y in range(5):
        return True
    return False

def bfs(i, j, place):
    # (x,y)석에 앉은 사람과 다른 지원자 간의 거리 체크하기
    queue = deque()
    queue.append([i,j,0])
    visited = [[0 for _ in range(5)] for _ in range(5)]
    visited[i][j] = 1
    
    while queue:
        x, y, count = queue.popleft()
        
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if in_bound(nx,ny) and visited[nx][ny] != 1:
                if place[nx][ny] == "P":
                    # 맨해튼 거리 2 이하이면
                    if count + 1 <= 2:
                        return False
                elif place[nx][ny] == "O":
                    visited[nx][ny] = 1
                    queue.append([nx,ny,count+1])
    return True

def solution(places):
    answer = []
    
    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if bfs(i,j,place) == False:
                        flag = False
                        break
            if flag == False:
                break
        if flag == False:
            answer.append(0)
        else:
            answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))