def solution(prices):
    # answer = []
    
    # for i in range(len(prices)):
    #     answer.append(0)

    answer = [0] * len(prices)
        
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] = answer[i]+1
            if prices[i] > prices[j]:
                break
        
    return answer