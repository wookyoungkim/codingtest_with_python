def maxArea(self, height):
    start = 0
    end = len(height)-1
    answer = 0
    
    while start < end:
        volume = min(height[start], height[end])*(end-start)
        answer = max(answer, volume)
        
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
        
    return answer