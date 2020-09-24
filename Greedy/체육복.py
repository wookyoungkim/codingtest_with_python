def solution(n, lost, reserve):
    answer = 0
    count = n - len(lost)
    lost.sort()
    reserve.sort()
    lost_students = []
    
    print(count)
    for l in lost:
        if l not in reserve:
            lost_students.append(l)
        else:
            reserve.remove(l)
            count += 1
    print(lost_students, reserve)
    
    for l in lost_students:
        if l-1 in reserve:
            count += 1
            reserve.remove(l-1)
            print(reserve)
        elif l+1 in reserve:
            count += 1
            reserve.remove(l+1)
            print(reserve)
            
    return count