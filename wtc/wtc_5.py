def solution(penter, pexit, pescape, data):
    answer = ''
    
    #문자열 penter의 길이만큼 자르기
    split_data = list(map(''.join, zip(*[iter(data)]*len(penter))))
    
    for s in split_data:
        if s in [penter, pexit, pescape]:
            answer += pescape
        answer += s
    
    return penter+answer+pexit