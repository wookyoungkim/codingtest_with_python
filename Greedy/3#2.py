#곱하기 혹은 더하기

def solution():
    num = input()
    result = int(num[0])

    for i in range(1, len(num)):
        #0또는 1이면 더하는게 이득
        if num[i] <=1 or result <=1:
            result += num
        else:
            result *= num

    print(result)

solution()



    

