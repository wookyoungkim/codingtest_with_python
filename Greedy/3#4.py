#만들 수 없는 금액 
# #####잘 모르겠다, , ,
from itertools  import combinations

def solution():
    N = int(input())
    ans = []
    coins = list(map(int, input().split()))
    coins.sort()

    print(coins)
    target = 1
    for x in coins:
        if target < x:
            break
        target += x
        print(target)
        
    
    
print(solution())


