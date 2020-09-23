#모험가길드
def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    answer = []

    arr.sort()
    while arr:
        team = []
        team.append(arr.pop(0))

        while team[0] > len(team):
            team.append(arr.pop(0))
            #print(team)
        
        if team[len(team)-1] <=len(team):
            answer.append(team)
            #print(answer)
    
    return len(answer)



solution()