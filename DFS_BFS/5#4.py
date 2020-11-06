def checkRight(p):
    flag = 0
    for i in range(len(p)):
        if p[i] == "(":
            flag += 1
        else:
            flag -= 1
        if flag < 0:
            return False
    return True

def checkBalanced(p):
    flag = 0
    for i in range(len(p)):
        if p[i] == "(":
            flag += 1
        else:
            flag -= 1
        if flag == 0:
            return i
    return len(p)-1

def dfs(p):
    answer = ''
    if p == '':
        return ''
    idx = checkBalanced(p)
    u = p[:idx+1]
    v = p[idx+1:]

    if checkRight(u):
        u += dfs(v)
        return u
    else:
        w = '('
        w += dfs(v)
        w += ')'
        for i in range(1, len(u)-1):
            if u[i] == "(":
                w += ')'
            else :
                w += '('
        return w


def solution(p):
    answer = ''
    if checkRight(p):
        return p
    else:
        answer = dfs(p)
        return answer


print(solution("()))((()"))
