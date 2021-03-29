import sys

input = sys.stdin.readline

#경사로 놓을 수 있는지?
def check(b):
    # 경사로 놓였으면 1, 아니면 0
    slope = [0 for _ in range(N)]
    for i in range(N-1):
        if abs(b[i]-b[i+1]) > 1:
            # 1이상 차이나면 놓을 수 없음
            return False
        
        if b[i] == b[i+1]:
            continue

        # 내리막길 경사로
        if b[i] > b[i+1]:
            pre = b[i+1]
            for j in range(i+1,i+1+L):
                if 0 <= j < N:
                    # 경사로를 설치 할 길이 같은 높이가 아닐 경우
                    if b[j] != pre: 
                        return False
                    # 이미 경사로 설치 한 경우
                    if slope[j] == 1: 
                        return False
                    # 경사로 설치
                    slope[j]=1
                else: 
                    return False
        # 오르막길 경사로
        else:
            pre = b[i]
            for j in range(i,i-L,-1):
                if 0 <= j < N:
                    # 경사로를 설치 할 길이 같은 높이가 아닐 경우
                    if b[j] != pre: 
                        return False
                    # 이미 경사로 설치 한 경우
                    if slope[j] == 1: 
                        return False
                    # 경사로 설치
                    slope[j] = 1
                else:
                    return False
    return True

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
for b in board:
    if check(b): 
        #경사로 놓을 수 있는지
        result+=1

#세로 길 확인하기
for b in list(map(list,zip(*board))):
    if check(b): 
        result+=1
print(result)