def solution(a):
    answer = len(a)
    mi = [0] * len(a)
    ma = [0] * len(a)

    # mi[i] : a[:i]까지의 최소
    # ma[i] : a[i:]까지의 최소
    min_val = a[0]
    for i in range(len(a)):
        if min_val >= a[i]:
            mi[i] = a[i]
            min_val = a[i]
        else:
            mi[i] = min_val

    min_val = a[-1]
    for i in range(len(a)-1, -1, -1):
        if min_val >= a[i]:
            ma[i] = a[i]
            min_val = a[i]
        else:
            ma[i] = min_val
    
    for i in range(len(a)):
        if a[i] > mi[i] and a[i] > ma[i]:
            answer -= 1
    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))