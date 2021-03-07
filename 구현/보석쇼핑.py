def solution(gems):
    answer = [1, len(gems)]
    length = len(set(gems))
    
    start, end = 0, 0

    while start <= len(gems) and end <= len(gems):
        if len(set(gems[start:end])) == length:
            if answer[1] - answer[0] > (end - start)-1:
                answer = [start+1, end]
            start += 1
        else:
            end += 1
    return answer

print(solution(["A", "A", "B"]))