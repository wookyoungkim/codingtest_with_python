def solution(logs):
    answer = []
    students = {}
    
    for log in logs:
        l = list(log.split())
        if l[0] not in students.keys():
            students[l[0]] = {}
        students[l[0]][l[1]] = l[2]
    
    for i in range(len(students)):
        for j in range(i+1, len(students)):
            student_1 = list(students.keys())[i]
            student_2 = list(students.keys())[j]
            
            if len(students[student_1]) == len(students[student_2]) and len(students[student_1])>=5:
                s_1 = sorted(students[student_1].items())
                s_2 = sorted(students[student_2].items())
                if s_1 == s_2:
                    if student_1 not in answer:
                        answer.append(student_1)
                    if student_2 not in answer:
                        answer.append(student_2)
    
    return sorted(answer) if len(answer) != 0 else ['None']