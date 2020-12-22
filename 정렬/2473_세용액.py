import sys

input = sys.stdin.readline
N = int(input())
solution = list(map(int, input().split()))
solution.sort()
answer = []
min_val = float('inf')

#세 용액중 하나를 기준으로 잡고 양끝의 투포인터 이동하면서 값 비교
for i in range(N-2):
    #이전 기준이랑 값이 같으면 굳이 한번 더 비교할 필요 없으므로
    if i>0 and solution[i] == solution[i-1]:
        continue
    start, end = i+1, N-1
    while start < end:
        total = solution[i] + solution[start] + solution[end]
        if abs(total) < abs(min_val):
            min_val = total
            answer = [solution[i], solution[start], solution[end]]
        #sum의 값이 작으면 start를 오른쪽으로 옮겨서 커지게
        if total < 0:
            start += 1
        #sum의 값이 크면 end를 왼쪽으로 옮겨서 작아지게
        elif total > 0:
            end -= 1
        else:
            answer = [solution[i], solution[start], solution[end]]
            break
for ans in answer:
    print(ans, end=" ")