import sys
input = sys.stdin.readline
maxval = -1000000001
minval = 1000000001

n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))


def dfs(i, result):
    global maxval, minval
    if i == n:
        minval = min(minval, result)
        maxval = max(maxval, result)
    else:
        #더하기
        if oper[0] > 0:
            oper[0] -= 1
            dfs(i+1, result + nums[i])
            oper[0] += 1

        #빼기
        if oper[1] > 0:
            oper[1] -= 1
            dfs(i+1, result - nums[i])
            oper[1] += 1

        #곱하기
        if oper[2] > 0:
            oper[2] -= 1
            dfs(i+1, result * nums[i])
            oper[2] += 1

        #나누기
        if oper[3] > 0:
            oper[3] -= 1
            dfs(i+1, int(result / nums[i]))
            oper[3] += 1

dfs(1, nums[0])
print(maxval)
print(minval)
    
    