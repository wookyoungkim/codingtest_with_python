answer = 0
target = None
def dfs(val, number):
    global answer
    if len(number) == 0: 
        if val == target:
            print("=", val)
            answer += 1
        return
    else:
        n = number.pop(0)
        dfs(val+n, number)
        dfs(val-n, number)
        number.insert(0, n)

def solution(number, t):
    global answer, target
    target = t
    dfs(0, number)
    return answer

solution([1,1,1,1,1], 3)