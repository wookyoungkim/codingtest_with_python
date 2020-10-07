def possible(answer):
    for x,y,a in answer:
        if a == 0:
            #기둥이면
            if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1 0] in answer:
                continue
            return False
        elif a == 1:
            #보이면
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x, y, a, b = i
        if b == 0:
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
        if b == 1:
            answer.append([x, ,y a])
            if not possible(answer):
                answer.remove([x, y, a])
        
    return answer