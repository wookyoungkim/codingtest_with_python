import sys
input = sys.stdin.readline

def solution(array):
    answer = [-1 for _ in range(len(array))]

    for i in range(len(array)):
        right = i+1

        while True:
            if right < len(array):
                if array[right] > array[i]:
                    answer[i] = array[right]
                    break
            right = right+1
            if right >= len(array):
                break
    return answer

N = int(input())
num = list(map(int, input().split()))
answer = solution(num)

for a in answer:
    print(a, end=" ")