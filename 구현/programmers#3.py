def solution(brown, yellow):
    answer = []
    if yellow == 1:
        return [3,3]
    for height in range(1, yellow//2+1):
        #print(height, int(yellow/height))
        if yellow%height == 0:
            if 2*height + 2*(yellow/height) + 4 == brown:
                return [yellow/height+2, height+2]
    return answer