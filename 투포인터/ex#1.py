n = 5 #데이터의 개수
m = 5 #특정 부분 합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

#start를 차례로 증가시켜나가기
for start in range(n):
    #end를 가능한 만큼 이동
    while interval_sum < m and end < n:
        end += 1
    #부분합과 같아지면
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
print(coount)