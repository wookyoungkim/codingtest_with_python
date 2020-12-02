import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def solution(bridge_length, weight, truck_weights):
    time = 0
    ntruck = 0
    current_weight = 0
    position = [0]*len(truck_weights)
    waiting = truck_weights[:]
    
    while len(waiting) != 0:
        print(time, ntruck, position, current_weight)
        for truck in range(ntruck):
            #지금까지 올라온 트럭들 위치 업데이트
            if position[truck] != -1:
                position[truck] += 1
                if position[truck] > bridge_length:
                    #다 건너면 총 무게에서 빼기
                    current_weight -= truck_weights[truck]
                    waiting.pop(0)
                    position[truck] = -1
                    
        #다음 트럭이 올라와도 감당 가능하면 
        if ntruck < len(truck_weights):
            if current_weight + truck_weights[ntruck] <= weight:
                #현재 무게 업데이트
                current_weight += truck_weights[ntruck]
                #ntruck번째 트럭까지 올라옴
                position[ntruck] = 1
                ntruck += 1

        time += 1

    return time

solution(2,	10,	[7,4,5,6])

#다른풀이
def solution(bridge_length,weight,truck_weights):
    time = 0
    bridge_on = [0]* bridge_length  #다리 표현
    curr_weight = 0 #현재 다리에 올라와 있는 무게
    
    while truck_weights:
        time+=1
        bridge_out = bridge_on.pop(0)   #다음에 빠질 트럭의 무게
        curr_weight -= bridge_out   
        #print(time," : ", bridge_out, curr_weight)

        if curr_weight + truck_weights[0] > weight: #무게초과면
            bridge_on.append(0)        #그냥 밀기
        else:
            truck = truck_weights.pop(0)        #다음에 올라올 트럭무게 
            bridge_on.append(truck)             #다리에 올리기
            curr_weight += truck
        print(bridge_on)


    while curr_weight>0:        #남은 무게 다 지날때까지 
        answer +=1
        bridge_out = bridge_on.pop(0)
        curr_weight -=bridge_out

    return answer
