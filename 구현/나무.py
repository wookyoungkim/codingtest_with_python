import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [] # 매년 추가될 양분의 양 저장
count = M # 총 나무의 수
for i in range(N):
    A.append(list(map(int, input().split())))
food = [[5]*N for _ in range(N)] #food[i][j]: (i.j)에 저장된 양분의 양
trees = [[[] for _ in range(N)] for _ in range(N)] # trees[i][j]: (i,j)에 있는 나무 나이 리스트
for i in range(M):
    x, y, z = map(int, input().split())
    heapq.heappush(trees[x-1][y-1], z)

for year in range(K):
    # 봄 & 여름
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                # 나이만큼 양분 먹기
                for t in range(len(trees[i][j])):
                    age = trees[i][j][t]
                    if food[i][j] - age < 0:
                        # 나이만큼 먹을 양분이 없으면
                        tree = list(trees[i][j])
                        del_tree = tree[t:] # 죽은 나무 -> 양분으로
                        for d in del_tree:
                            food[i][j] += d//2
                        pos_tree = tree[:t] # 살아남은 나무
                        trees[i][j] = pos_tree
                        count -= len(del_tree)
                        break
                    else:
                        food[i][j] -= age
                        trees[i][j][t] += 1
    
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    # 가을
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for t in trees[i][j]:
                    if t%5 == 0:
                        for k in range(8):
                            nx, ny = i+dx[k], j+dy[k]
                            # 8방향으로 번식
                            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                                continue
                            else:
                                trees[nx][ny].insert(0,1)
                                count += 1
    # 겨율
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

print(count)