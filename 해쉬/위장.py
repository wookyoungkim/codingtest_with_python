def solution(clothes):
    answer = 1
    dic = {}
    cloth_type = []
    
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1
            cloth_type.append(cloth[1])
    
    for i in range(len(cloth_type)):
        answer *= (dic[cloth_type[i]]+1)

    return answer-1