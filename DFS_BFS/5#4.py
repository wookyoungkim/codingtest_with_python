def right(p):
    flag = 0
    for i in range(len(p)):
        


def solution(p):
    answer = ''
    if p == '':
        return ''
    while True:
        balanced = list(p)
        u, v = '', ''
        flag = 0
        for i in range(len(balanced)):
            if balanced[i] == '(':
                flag -= 1
            else:
                flag += 1
            if flag == 0:
                u = balanced[:i]
                v = balanced[i+1:]
                break
        print(u, v)
    return answer