n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

#리스트 A와 B의 모든 원소를 담을 수 있는 리스트 초기화
result = [0]*(n+m)
i, j, k = 0

while i<n and j<m:
    #B가 전부 처리되었거나 A의 원소가 더 작을 때
    if j>=m or (i<n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)