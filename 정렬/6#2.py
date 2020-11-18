N = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[(N-1)//2])
