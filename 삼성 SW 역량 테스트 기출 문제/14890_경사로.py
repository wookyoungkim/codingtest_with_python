import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
answer = 0

def check_vertical(slope):
    vertical_count = 0
    #가로 확인하기
    for i in range(N):
        count = 1 #연속된 k개의 낮은 칸 확인
        flag = 0
        countable = True
        for j in range(N-1):
            #i와 i+1이 같은 경우
            if board[i][j] == board[i][j+1]:
                #i보다 i+1이 작은 경우에서 앞으로의 L개 높이 체크하는 경우
                count += 1
                if flag == 1:
                    if count == L:
                        #경사로 설치하기
                        for k in range(count):
                            slope[i][j-k] = 1
                        flag = 0
                        count = 1
            #i가 i+1보다 작은 경우
            elif board[i][j]+1 == board[i][j+1]:
                if flag == 1:
                    countable = False
                    break
                if count >= L:  #i까지 L개의 높이가 같았어야 경사로 설치 가능
                    for k in range(count):
                        slope[i][j-k] = 1
                    count = 1
                    continue
                else:
                    countable = False
                    break   #해당 길에서 경사로 설치가 불가능하면 뒤에 더 볼 필요 x
            #i가 i+1보다 작은 경우
            elif board[i][j] == board[i][j+1]+1:
                if flag == 1:
                    countable = False
                    break
                #앞으로의 L개의 높이가 같아야 세울 수 있음
                count = 1
                flag = 1
            else:
                countable = False
                break #해당 길에서 경사로 설치가 불가능하면 뒤에 더 볼 필요 x
        #포문을 끝까지 돌고 조건을 전부 만족했으면
        if countable == True:
            print("v: ", i)
            vertical_count += 1
    return vertical_count
            
def check_horizontal(slope):
    horizontal_count = 0
    #세로 확인하기
    for i in range(N):
        count = 1 #연속된 k개의 낮은 칸 확인
        flag = 0
        countable = True
        for j in range(N-1):
            #i와 i+1이 같은 경우
            if board[j][i] == board[j+1][i]:
                #i보다 i+1이 작은 경우에서 앞으로의 L개 높이 체크하는 경우
                count += 1
                if flag == 1:
                    if count == L:
                        for k in range(count):
                            slope[i][j-k] = 1
                        #경사로 설치 가능
                        flag = 0
                        count = 1
            #i가 i+1보다 작은 경우
            elif board[j][i]+1 == board[j+1][j]:
                if flag == 1:
                    countable = False
                    break
                if count >= L:  #i까지 L개의 높이가 같았어야 경사로 설치 가능
                    for k in range(count):
                        slope[i][j-k] = 1
                    count = 1
                    continue
                else:
                    countable = False
                    break   #해당 길에서 경사로 설치가 불가능하면 뒤에 더 볼 필요 x
            #i가 i+1보다 작은 경우
            elif board[j][i] == board[j+1][i]+1:
                if flag == 1:
                    countable = False
                    break
                #앞으로의 L개의 높이가 같아야 세울 수 있음
                count = 1
                flag = 1
            else:
                countable = False
                break #해당 길에서 경사로 설치가 불가능하면 뒤에 더 볼 필요 x
        #포문을 끝까지 돌고 조건을 전부 만족했으면
        if countable == True:
            print("h: ", i)
            horizontal_count += 1
    return horizontal_count

slope1 = [[0]*(N) for _ in range(N)]
print("h->v")
ans1 = check_horizontal(slope1) + check_vertical(slope1)

print("v->h")
slope2 = [[0]*(N) for _ in range(N)]
ans2 = check_vertical(slope2) + check_horizontal(slope2)

print(ans1, ans2)