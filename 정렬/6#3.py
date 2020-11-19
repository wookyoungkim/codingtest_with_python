def solution(N, stages):
    answer = []
    ans = {}
    
    for i in range(1, N+1):
        total_players = 0
        for j in stages:
            if j>=i:
                total_players += 1
        ans[i] = stages.count(i)/total_players if total_players != 0 else 0
    return sorted(ans, key=lambda x : ans[x], reverse=True)