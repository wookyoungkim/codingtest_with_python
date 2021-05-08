def solution(s):
    answer = ''
    ntos = {"zero":"0", "one":"1", "two":"2", "three":"3", 
            "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    i=0
    while i < len(s):
        if s[i] in ntos.values():
            answer += s[i]
            i += 1
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