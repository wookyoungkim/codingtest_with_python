def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    trash = []
    bottom = n-1
    cur = int(k)
    
    for c in cmd:
        if c[0] == "U":
            command, x = c.split()
            cnt = 1
            while cnt <= int(x):
                cur = (cur-1)%n
                if answer[cur] == "O":
                    cnt += 1
            
        elif c[0] == "D":
            command, x = c.split()
            cnt = 1
            while cnt <= int(x):
                cur = (cur+1)%n
                if answer[cur] == "O":
                    cnt += 1

        elif c[0] == "C":
            answer[cur] = 'X'
            trash.append(cur)

            if cur == bottom:
                # 가장 아래 행이었으면
                cur = (cur-1)%n
                while answer[cur] != 'O':
                    cur = (cur-1)%n
                bottom = cur
            else:
                cur = (cur+1)%n
                while answer[cur] != 'O':
                    cur = (cur+1)%n

        else:
            answer[trash[-1]] = 'O'
            if bottom < trash[-1]:
                bottom = trash[-1]
            trash.pop()

    return ''.join(answer)