import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - a)/b) for a,b in zip(progresses, speeds)]
    print(days)
    front = 0
    for i in range(len(days)):
        if days[front] < days[i]:
            print(str(i) +' '+str(front))
            answer.append(i-front)
            front = i
    answer.append(len(days)-front)
    
    return answer