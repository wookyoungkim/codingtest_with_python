def solution(participant, completion):
    answer = ''
    
    completion.sort()
    participant.sort()
    
    for i in range(len(completion)): 
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    if answer == '':
        answer = participant[len(completion)]
    
    return answer

#다른풀이

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer