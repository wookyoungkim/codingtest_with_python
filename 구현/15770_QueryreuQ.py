import sys
from collections import defaultdict
input = sys.stdin.readline

Q = int(input())
query = input().strip()
answer = [0 for _ in range(len(query))]
n_pellindrom = defaultdict()
S = ''

def ispellindrom(string):
    # 문자열이 추가됨으로서 펠린드롬이 생기는지?
    count = 0
    for i in range(len(string)):
        tmp = string[i:]
        left, right = 0, len(tmp)-1
        flag = True

        while left < right:
            if tmp[left] != tmp[right]:
                flag = False
                break
            left  += 1
            right -= 1 
        if flag == True:
            count += 1
    return count

        
for i in range(len(query)):
    pre = S
    count = 0
    # 연산하기
    if query[i] == '-':
        # 지우기 연산에는 펠린드롬 계산할 필요 x
        S = S[:-1]
    else:
        tmp = 0
        if S != '':
            tmp = n_pellindrom[S]
        S += query[i]
        n_pellindrom[S] = tmp + ispellindrom(S)
    print(n_pellindrom[S], end=' ')