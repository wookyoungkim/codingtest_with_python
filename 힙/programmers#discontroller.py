import heapq
def solution(jobs):
    in_time = -1
    out_time = 0
    n = len(jobs)
    jobs.sort(key = lambda k:k[0])
    heap = []           
    time = []
    sum = 0
    count = 0
                
    while count < n:
        for job in jobs:
            if in_time < job[0] <= out_time:
                heapq.heappush(heap, [job[1], job[0]])
        
        if len(heap) > 0:
            job = heapq.heappop(heap)
            in_time = out_time
            out_time += job[0]
            count += 1
            time.append(out_time-job[1])
        
        else:
            out_time += 1

    for t in time:
        sum += t
    
    return int(sum/n)