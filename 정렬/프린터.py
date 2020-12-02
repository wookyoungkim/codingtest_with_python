import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def solution(priorities, location):
    pi_list = list(enumerate(priorities))
    #print(pi_list)
    waiting_q = []

    while pi_list:
        pi = pi_list.pop(0)
        priority = pi[1]
        p_list = [priority for idx, priority in pi_list]

        #print(p_list)
        if p_list:
            max_p = max(p_list)

        if priority >= max_p:
            waiting_q.append(pi)
        else:
            pi_list.append(pi)

    #print(waiting_q)
    for i in range(len(waiting_q)):
        if location == waiting_q[i][0]:
            return i+1

solution([2, 1, 3, 2],	2)

#다른풀이

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    print(queue)
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            print(queue)
        else:
            answer += 1
            print(answer)
            if cur[0] == location:
                return answer

