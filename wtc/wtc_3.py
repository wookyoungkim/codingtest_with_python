def solution(money, expected, actual):
    betting = 100
    for i in range(len(expected)):
        #print(expected[i], actual[i], betting, end=' ')
        if expected[i] == actual[i]:
            money += betting
            betting = 100
        else:
            money -= betting
            if money <= betting*2:
                betting = money
            else:
                betting += betting
        #print(money)
    return money