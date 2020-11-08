def operators(s1, s2, op):
    if op == '+':
        return s1+s2
    elif op == '-':
        return s1-s2
    else:
        return s1*s2

def solution(s, op):
    answer = []
    for i in range(len(s)-1):
        answer.append(operators(int(s[:i+1]), int(s[i+1:]), op))
    return answer