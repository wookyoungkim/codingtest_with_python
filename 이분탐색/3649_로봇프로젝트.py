import sys 

input = sys.stdin.readline

while True:
    try:
        x = int(input())* pow(10,7)
        n = int(input())
        lego = []
        for _ in range(n):
            lego.append(int(input()))

        # 1. 정렬하기
        lego.sort()

        # 2. 투포인터로 탐색
        left, right = 0, len(lego)-1
        flag = False

        while left < right :
            if lego[left] + lego[right] == x:
                flag = True
                print("yes", str(lego[left]), str(lego[right]))
                break
            elif lego[left] + lego[right] > x:
                right -= 1
            else:
                left += 1

        if flag == False:
            print("danger")
    except:
        break