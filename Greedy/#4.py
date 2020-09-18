#1이 될 때까지
def solution():
    N, K = map(int, input().split())
    count = 0

    while N != 1:
        if N % K == 0:
            N = N//K
            count += 1
        else:
            N -= 1
            count += 1
    print(count)

solution()