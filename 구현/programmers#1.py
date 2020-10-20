def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    score = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == student1[i%len(student1)]:
            score[1] += 1
        if answers[i] == student2[i%len(student2)]:
            score[2] += 1
        if answers[i] == student3[i%len(student3)]:
            score[3] += 1
    
    if max(score[1], score[2], score[3]) == score[1]:
        answer.append(1)
    if max(score[1], score[2], score[3]) == score[2]:
        answer.append(2)
    if max(score[1], score[2], score[3]) == score[3]:
        answer.append(3)
    answer.sort()
    return answer