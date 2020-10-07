def solution():
    time = 0
    length = 1
    direction = 1
    head_position = [0,0]
    tail_position = [0,0]
    snake = [[1,1]]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1] #북동남서
    dir_dic = {}

    N = int(input())
    K = int(input())
    board = [[0]*(N) for _ in range(N)]

    for _ in range(K):
        x,y = map(int, input().split())
        board[x-1][y-1] = 1
    board[0][0] = 2

    L = int(input())
    for _ in range(L):
        x,c = input().split()
        dir_dic[int(x)] = c

    while True:
        #print(time, ": ", head_position, tail_position, direction)
        for i in range(len(board)):
            #print(board[i])

         #방향이동 있으면
        if time in dir_dic.keys():
            if dir_dic[time] == 'D':
                direction = (direction+1)%4
                del dir_dic[time]
            else:
                direction = (direction+3)%4
        time += 1
          
        #머리 이동시키기
        head_position[0] += dx[direction]
        head_position[1] += dy[direction]
        snake.append([head_position[0], head_position[1]])
       
        if head_position[0]<0 or head_position[0]>=N or head_position[1]<0 or head_position[1]>=N:
            #print("out of board")
            break
        #이동시킨 위치에 뱀 몸 있으면
        elif board[head_position[0]][head_position[1]] == 2:
            break
        else:
            #이동시킨 위치에 사과 있으면
            if board[head_position[0]][head_position[1]] == 1:
                length += 1
            #이동시킨 위치에 사과 없으면
            else:
                #print(head_position, tail_position)
                board[tail_position[0]][tail_position[1]] = 0
                snake.pop(0)
                tail_position[0] = snake[0][0]
                tail_position[1] = snake[0][1]
            board[head_position[0]][head_position[1]] = 2

    return time   
 
print(solution())
