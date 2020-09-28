def solution():
    N = input()
    frt = []
    back = []
    for i in range(len(N)):
        if i < len(N)/2:
            frt.append(int(N[i]))
        else:
            back.append(int(N[i]))
    if sum(frt) == sum(back):
        print("LUCKY")
    else:
        print(READY)

solution()