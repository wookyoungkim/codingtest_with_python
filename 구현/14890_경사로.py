import sys
import copy

input = sys.stdin.readline

answer = 0
N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def possible(road):
    count = 0
    flag = False
    slope = []
    s = []
    for i in range(N-1):
        print(s)
        if flag == True:
            #road[i] == road[i+1]-1이라서 L개 넘는지 세는 경우
            if count == L:
                count = 0
                flag = False
                s = []
                slope += s
            elif road[i] == road[i+1]:
                count += 1
                s.append(i)
            else:
                return []
        else:
            s.append(i)
            if road[i] == road[i+1]:
                count += 1
            elif road[i]+1 == road[i+1]:
                #왼쪽에 경사로 놓을 수 있는지?
                if count+1 >= L:
                    slope.append(s)
                    s = []
                    count = 0
                else:
                    return []
            elif road[i] == road[i+1]+1:
                #오른쪽에 경사로를 놓을 수 있는지?
                flag = True
            else:
                return []
    return slope

print(possible(board[3]))

# {horizontal}의 road번째 길에 경사로 놓기
def dfs(horizontal, road, slope, count):
    if not horizontal and road == N:
        answer = max(answer, count)
        return 

    if horizontal:
        result = copy.deepcopy(board[road])
    else:
        result = []
        for i in range(N):
            result.append(board[i][road])

    #가로 road번째 길 검사하기
    slopes, pos = possible(result)
    if pos:
        #경사로 놓기
        if road+1 >= N:
            dfs(0, 0, slope+slopes, count)
        else:
            dfs(horizontal, road + 1, slope+slopes, count)
    if road+1 >= N:
            dfs(0, 0, slope, count)
    else:
        dfs(horizontal, road + 1, slope, count)
#dfs(0, 0, [], 0)
