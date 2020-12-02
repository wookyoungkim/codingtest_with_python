def solution(citations):
    citations.sort()
    length = len(citations)
    print(citations, length)
    
    for i in range(length):
        #citations[i]: i번 인용, length-i: i번이상 인용된 논문 개수
        if citations[i] >= length-i:
            return length-i
    return 0


#다른 풀이

# def solution(citations):
#     citations.sort(reverse=True)
#     b = enumerate(citations, start=1)
#     print(b)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer