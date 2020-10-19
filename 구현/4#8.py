def fixing(N, weak, dist, fixed, count, num):
    #i번째 친구부터 체크하기
    if 0 not in fixed.values():
        return True
    if num >= count:
        return False
    print(count, "명의 친구: ")
    for w in weak:
        if fixed[w] != 1:
            #k부터 idx까지 전부 수리 완료 
            idx = w + dist[num]
            if idx > N:
                for l in weak: 
                    if l in range(0, idx%N+1):
                        fixed[l] = 1
                    elif l in range(w,N-1):
                        fixed[l] = 1
            else:
                for l in weak:
                    if l in range(w,idx+1):
                        fixed[l] = 1
            #print(num, ": ", w, "- ", fixed)
            if fixing(N, weak, dist, fixed, count, num+1):
                return True
            if idx > N:
                for l in weak: 
                    if l in range(0, idx%N+1):
                        fixed[l] = 0
                    elif l in range(w,N-1):
                        fixed[l] = 0
            else:
                for l in weak:
                    if l in range(w,idx+1):
                        fixed[l] = 0
            

def solution(n, weak, dist):
    dist.sort(reverse=True)
    fixed = {}
    for w in weak:
        fixed[w] = 0

    for i in range(1, len(dist)+1):
        #i명의 친구가 점검하는 경우
        if fixing(n, weak, dist, fixed, i, 0):
            return i

    return -1

print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))