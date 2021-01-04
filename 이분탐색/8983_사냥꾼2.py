import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
hunters = list(map(int, input().split()))
animals = []
for _ in range(N):
    animals.append(list(map(int, input().split())))

hunters.sort()
animals.sort()
answer = 0

for animal in animals:
    start, end = 0, len(hunters)-1
    while start <= end:
        mid = (start+end)//2
        dist = abs(hunters[mid]-animal[0])+animal[1]

        #해당 사대에서 사격 가능하면
        if dist <= L:
            answer += 1
            break
        else:
            if hunters[mid] < animal[0]:
                start = mid+1
            else:
                end = mid-1
print(answer)