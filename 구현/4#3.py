def solution(s):
    length = len(s)
    answer = length
    
    for l in range(1, length//2+1):
        compressed = ""
        count = 1
        #주어진 문자열을 1개부터 length//2개단위로 자르기
        lst = [s[i:i+l] for i in range(0, len(s), l)]
        prev = lst[0]

        for i in range(1, len(lst)):
            if prev == lst[i]:
                count += 1
            else:
                compressed += str(count) +prev if count>=2 else prev
                count = 1
                prev = lst[i]
                print(compressed)

        compressed += str(count) +prev if count>=2 else prev
        answer = min(answer, len(compressed))

    return answer

print(solution("aabbaccc"))