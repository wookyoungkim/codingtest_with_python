#숫자 카드 게임

def solution():
    N, M = map(int, input().split())
    data = []
    maxval = 0
    maxindex = -1

    for i in range(N):
        arr = list(map(int, input().split()))
        if min(arr) > maxval:
            maxval = min(arr)
    print(maxval)

solution()