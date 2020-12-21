import sys

input = sys.stdin.readline

tests = []
answer = []

tc = int(input())
#각 테스트 케이스를 길이별로 정렬해서 저장
for _ in range(tc):
    num = int(input())
    tmp = []
    for num in range(num):
        tmp.append(input().strip())
    tmp.sort()
    tests.append([num, tmp])
print(tc, tests)

for test in tests:
    n, tels = test
    flag = 0
    #print(n, tels)
    for i in range(len(tels)-1):
        if tels[i] == tels[i+1][:len(tels[i])]:
            flag = -1
            break
    if flag == -1:
        answer.append("NO")
    else:
        answer.append("YES")

for ans in answer:
    print(ans)