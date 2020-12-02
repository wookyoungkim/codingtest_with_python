import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for i in scoville:
        heapq.heappush(heap, i)
        
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first+second*2)
        answer += 1
    
    return answer