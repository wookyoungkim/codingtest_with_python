# 구현
def solution(s):
    answer = ''
    ntos = {"zero":"0", "one":"1", "two":"2", "three":"3", 
            "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    i=0
    while i < len(s):
        # 그냥 숫자면?
        if s[i] in ntos.values():
            answer += s[i]
            i += 1
        # 문자로 주어지면 -> 잘라서 key와 비교하기
        else:
            if s[i:i+3] in ntos.keys():
                answer += str(ntos[s[i:i+3]])
                i += 3
            elif s[i:i+4] in ntos.keys():
                answer += str(ntos[s[i:i+4]])
                i += 4
            else:
                answer += str(ntos[s[i:i+5]])
                i += 5
    return int(answer)

print(solution("0zero1fivenine"))