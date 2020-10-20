import itertools
import math

def isPrime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    return False

def solution(numbers):
    answer = 0
    number = []
    
    for i in range(1, len(numbers)+1):
        num = list(itertools.permutations(numbers, i))
        for n in num:
            number.append(int(''.join(n)))
    number = list(set(number))

    #for i in range(len(numbers)):
    #   set(map(int, map("".join, permutations(list(n), i + 1))))

    for n in number:
        if isPrime(int(n)) == True:
            answer += 1
    return answer

print(solution('011'))


#다른풀이
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#         print(a)
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)