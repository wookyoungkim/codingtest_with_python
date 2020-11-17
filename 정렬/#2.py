N = int(input())
dic = {}

for _ in range(N):
    student, score = input().split()
    dic[student] = int(score)

sorted_dic = sorted(dic.items(), key= lambda k: k[1])
print(sorted_dic)
for st, sc in sorted_dic:
    print(st, end=" ")