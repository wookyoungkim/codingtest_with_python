from bisect import bisect_left

def binary_search(lst, key):
    start, end = 0, len(lst)-1
    
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return end

def solution(info, query):
    answer = []
    languages = ["cpp", "java", "python", "-"]
    job_group = ["backend", "frontend", "-"]
    career = ["junior", "senior", "-"]
    food = ["chicken", "pizza", "-"]
    applicants = {}
    scores = []
    
    for l in languages:
        for j in job_group:
            for c in career:
                for f in food:
                    str1 = l+j+c+f
                    applicants[str1] = []
    
    for i in range(len(info)):
        l, j, c, f, score = info[i].split(" ")
        scores.append(score)
        for ll in [l, "-"]:
            for jj in [j, "-"]:
                for cc in [c, "-"]:
                    for ff in [f, "-"]:
                        applicants[ll+jj+cc+ff].append(int(score))
    for a in applicants.values():
        a.sort()
        
    for q in query:
        count = 0
        l, j, c, f, score = list(q.replace("and ", "").split(" "))
        idx = bisect_left(applicants[l+j+c+f], int(score))
        answer.append(len(applicants[l+j+c+f]) - idx)
        
    return answer