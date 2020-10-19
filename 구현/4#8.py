import itertools 

def solution(n, weak, dist):
    dist.sort(reverse=True)
    length = len(weak)

    #길이 2배인 일자 리스트로 바꾸기
    for i in range(length):
        weak.append(weak[i]+n)
    print(weak)
    answer = len(dist)+1

    #0부터 length-1까지 시작점
    for start in range(length):
        for friends in list(itertools.permutations(dist, len(dist))):
            #투입되는 친구의 수
            count = 1
            #해당 친구가 점검하는 마지막 위치
            position = weak[start] + friends[count-1]

            for index in range(start, start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
