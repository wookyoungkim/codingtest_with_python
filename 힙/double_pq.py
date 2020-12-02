import heapq

def solution(operations):
    answer = []
    
    for oper in operations:
        print("oper: "+oper)
        if oper[0] == "I":
            num = int(oper[2:])
            heapq.heappush(answer, num)
            print(answer)
            
        elif len(answer) != 0:
            if oper[2] == "-":
                heapq.heappop(answer)
                print(answer)
            else:
                answer.remove(max(answer))
                print(answer)
    
    if len(answer)==0:
        return [0,0]
    else:
        return [max(answer), answer[0]]