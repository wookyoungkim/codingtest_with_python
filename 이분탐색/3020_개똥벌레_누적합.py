import sys

input = sys.stdin.readline
N, H = map(int, input().split())
#구간 i에서
bottom = [0]*(H+1) #석순 -> 길이 i 이상면 부셔야함
top = [0]*(H+1) #종유석 -> 길이 N-i 이상이면 부셔야함
for _ in range(N//2):
    b = int(input().strip())
    bottom[b] += 1
    t = int(input().strip())
    top[t] += 1
min_val = [0]*N
answer = N
stone = [0]*(H+1)
for i in range(1, H+1):
    stone[i] = sum(bottom[i:])+sum(top[H-i+1:])
print(stone)