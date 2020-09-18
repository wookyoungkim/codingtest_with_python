#큰 수의 법칙

def solution():
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = 0
    
    arr.sort(reverse=True)

    for i in range(1, M+1):
        if i%K == 0:
            answer += arr[1]
        else:
            answer += arr[0]

    print(answer)

#수열로 풀이
def seq_solution():
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    #가장 큰 수가 더해지는 횟수 -> 수열의 총 길이:k+1
    count = int(M / (K+1)) * K
    #m이 k+1로 나누어 떨어지지 않는 경우의 나머지도 더해주기
    count += M%(K+1)

    result = 0
    result += count * arr[0]
    result += (M-count) * arr[1]

    print(result)

solution()
seq_solution()




