def solution(N, number):
    answer = -1
    
    if N == number:
        return 1
    
    #n을 1번부터 8번 사용한 set의 초기화
    s = [set() for _ in range(8)]
    for i,x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if  number in s[i]:
            answer = i + 1
            break

    return answer

print(solution(5,	12))