import sys

input = sys.stdin.readline

N = int(input())
time = []
profit = []
answer = 0
for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

def get_profit(day, total_profit):
    global answer
    if day == N:
        answer = max(answer, total_profit)
        return
    if day > N:
        return
    #오늘 일 하는 경우
    if day + time[day] <= N+1:
        get_profit(day+time[day], total_profit+profit[day])
    #오늘 일 안하는 경우
    if day + 1 <= N+1:
        get_profit(day+1, total_profit)

get_profit(0, 0)
print(answer)
