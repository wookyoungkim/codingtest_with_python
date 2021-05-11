import sys

input = sys.stdin.readline
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def in_bound(x, y):
    if x in range(N) and y in range(N):
        return True
    return False

N, M = map(int, input().split())
water = []
for _ in range(N):
    water.append(list(map(int, input().split())))
moves = []
for _ in range(M):
    moves.append(list(map(int, input().split())))

# 초기 구름 설정
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# M번 이동시키기
for d, s in moves:
    copying = set() # 구름이 이동한 좌표 저장 
    # 모든 구름 이동시키기 & 비내리기 & 지우기
    for _ in range(len(cloud)):
        x, y = cloud[0][0], cloud[0][1]
        nx, ny = (x+dx[d]*s)%N, (y+dy[d]*s)%N
        cloud.append((nx, ny)) # 구름 이동
        water[nx][ny] += 1 # 비내리기
        cloud.pop(0)
        copying.add((nx, ny))

    cloud = []
    # 물 복사 버그
    for x, y in copying:
        count = 0
        for d in range(2, 9, 2):
            nx, ny = x+dx[d], y+dy[d]
            if in_bound(nx, ny) and water[nx][ny]>0:
                count += 1
        water[x][y] += count
    
    # 구름 새로 생성
    for x in range(N):
        for y in range(N):
            if water[x][y] >= 2 and (x,y) not in copying:
                cloud.append((x,y))
                water[x][y] -= 2
answer = 0
for i in range(N):
    answer += sum(water[i])
print(answer)