#게임 개발

def solution():
    N, M = map(int, input().split())
    pos = list(map(int, input().split()))
    map_info = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    dir_count = 0
    count = 1

    for i in range(N):
        arr = list(map(int, input().split()))
        map_info.append(arr)
    map_info[pos[0]][pos[1]] = 2
    
    while True:
        if dir_count > 4:
            back = (pos[2]+2) % 4
            pos[1] += dx[back]
            pos[0] += dy[back]
            if map_info[pos[0]][pos[1]] == 1:
                break
            else:
                dir_count = 0
        #바라보는 방향 기준 왼쪽을 방문했는지 ? 
        left = (pos[2]+3)%4
        if map_info[pos[0]+dy[left]][pos[1]+dx[left]] == 0:
            #왼쪽 방문한적 없음
            pos[2] = left
            pos[1] += dx[pos[2]]
            pos[0] += dy[pos[2]]
            map_info[pos[0]][pos[1]] = 2
            count += 1
            dir_count = 0
            
        else:
            pos[2] = left
            dir_count += 1
            
        print("pos: ", pos, " count: ", dir_count)
        print(map_info)

    return count   

print(solution())
