import heapq

def solution(food_times, k):
    answer = 0
    food = []

    if sum(food_times) <= k:
        return -1

    for i in range(len(food_times)):
        heapq.heappush(food, (food_times[i], i+1))

    time = 0 #먹기위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간
    length = len(food_times)
    
    while time + ((food[0][0] - previous) * length) <= k:
        now = heapq.heappop(food)[0]
        time += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(food, key = lambda k : k[1])
    return result[(k-time) % length][1]  
print(solution([3, 1, 2],	5))