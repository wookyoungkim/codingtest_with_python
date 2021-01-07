import sys
import copy

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
answer = 0

for k in range(N):
    seq1 = copy.deepcopy(seq[:k+1])
    seq2 = copy.deepcopy(seq[k:])
    seq2.reverse()
    dp1 = [1]*(len(seq1)+1)
    dp2 = [1]*(len(seq2)+1)

    #LIS 알고리즘
    for i in range(1, len(seq1)):
        for j in range(0, i):
            if seq1[j] < seq1[i]:
                dp1[i] = max(dp1[i], dp1[j]+1)

    #LIS 알고리즘
    for i in range(1, len(seq2)):
        for j in range(0, i):
            if seq2[j] < seq2[i]:
                dp2[i] = max(dp2[i], dp2[j]+1)
    answer = max(answer, max(dp1)+max(dp2)-1)

print(answer)