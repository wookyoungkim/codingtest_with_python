def impossible(n, middle, times):
    #가능한 경우 : 각 심사대가 심사할 수 있는 최대 인원수의 합이 N이상인 경우
    return sum([middle // x for x in times]) < n

def solution(n, times):
    left, right = 1, min(times)*n
    while left < right:
        middle = (left + right) // 2
        print(left, right, middle)
        if impossible(n, middle, times): 
            left = middle + 1
        else: 
            right = middle
    return left


print(solution(6,	[7, 10]))