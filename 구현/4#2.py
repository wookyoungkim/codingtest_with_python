def solution():
    S = input()
    num = 0
    alph = []

    for s in S:
        if s.isalpha():
            alph.append(s)
        else:
            num += int(s)

    alph.sort()
    ans = "".join(alph)

    return ans +str(num)

print(solution())