def solution(n, k, cmd):
    answer = ["O" for _ in range(n)]
    table = [i for i in range(n)]
    trash = []
    cur = int(k)
    
    for c in cmd:
        if c[0] == "U":
            command, x = c.split()
            cur = (cur-int(x))%len(table)
            
        elif c[0] == "D":
            command, x = c.split()
            cur = (cur+int(x))%len(table)

        elif c[0] == "C":
            trash.append(table[cur])
            answer[table[cur]] = "X"
            del table[cur]
            if cur > len(table)-1:
                cur -= 1
        else:
            add = trash.pop()
            answer[add] = "O"
            if add < table[cur]:
                cur += 1
            start, end = 0, len(table)-1
            while start <= end:
                mid = (start+end)//2
                if table[mid] < add:
                    start = mid + 1
                else:
                    end = mid - 1
            table.insert(start, add)

    return ''.join(answer)

print(solution(8,	2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))