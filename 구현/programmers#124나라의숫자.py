def solution(n):
    answer = ''
    while n > 0:
        #print(n, answer)
        if n % 3 == 0:
            answer = '4' + answer
            n = n//3 -1
        else:
            if n % 3 == 1:
                answer = '1' + answer
            elif n % 3 == 2:
                answer = '2' + answer
            n //= 3
    return answer
print(solution(20))