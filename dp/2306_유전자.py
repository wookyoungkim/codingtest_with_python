import sys

input = sys.stdin.readline

def findKOI(start, end):
    isKOI = dp[start][end]
    if isKOI != -1:
        return isKOI
    
    isKOI = 0
    # 조건 2: aXt, gXc 인지? 
    if((dna[start] == 'a' and dna[end] == 't') or (dna[start] == 'g' and dna[end] == 'c')):
        isKOI = findKOI(start+1, end-1) + 2;
    
    for i in range(start, end):
        isKOI = max(isKOI, findKOI(start, i) + findKOI(i+1, end))
    
    dp[start][end] = isKOI
    return isKOI

dna = input()
dp = [[-1 for _ in range(len(dna))] for _ in range(len(dna))]
print(findKOI(0, len(dna)-1))