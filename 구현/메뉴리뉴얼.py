from itertools import combinations

def solution(orders, course):
    answer = []
    orders.sort(key=lambda x:len(x), reverse=True)
    max_len = len(orders[0])
    
    for c in course:
        if c <= max_len:
            dic = {}
            for order in orders:
                o_list = list(combinations(sorted(list(order)), c))
                for o in o_list:
                    str1 = ""
                    for i in o:
                        str1 += i
                    if str1 in dic.keys():
                        dic[str1] += 1
                    else:
                        dic[str1] = 1
            sorted_dic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
            
            if sorted_dic[0][1] != 1:
                answer.append(sorted_dic[0][0])
                for i in range(1, len(sorted_dic)):
                    if sorted_dic[i][1] == sorted_dic[0][1]:
                        answer.append(sorted_dic[i][0])
                    else:
                        break
    answer.sort()            
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]))