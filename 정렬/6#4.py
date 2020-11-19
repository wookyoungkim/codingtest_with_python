import heapq

N = int(input())
cards = []
answer = 0
for _ in range(N):
    heapq.heappush(cards, int(input()))

while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += (a+b)
    heapq.heappush(cards, a+b)

print(answer)