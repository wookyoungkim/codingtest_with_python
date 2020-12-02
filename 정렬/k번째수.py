def solution(array, commands):
    answer = []
    
    for num in range(len(commands)):
        arr = array[commands[num][0]-1:commands[num][1]]
        arr.sort()
        print(arr)
        answer.append(arr[commands[num][2]-1])
    
    return answer