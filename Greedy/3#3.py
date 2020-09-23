#문자열 뒤집기

def solution():
    string = list(map(int, list(input())))

    #0에서 1, 1에서 0으로 바뀌는 시점을 카운트하기

    if string[0] == 0:
        #전부 0으로
        count0 = 1
        #전부 1로
        count1 = 0
    else:
        count0 = 0
        count1 = 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == 1:
                count0 += 1
            else:
                count1 += 1

    return min(count0, count1)

print(solution())