# 구현을 사용해서 풀었다 ,,, 
# -> 직접 list에 넣고 뺄지, ox로 마크만 할지 고민하다가 insert시 전부 뒤로 밀어야 된다는 점에서 비효율적일것 같아 마크함
# 아예 구현으로 접근해서 그런지 다른 풀이를 떠올리지 못했다
# linked list를 이용해서 풀면 될것같다고 생각했는데, 클래스 선언, 삽입삭제 등의 구현이 복잡할 것같아서 여기서 개선시키려고 노력했다

def solution(n, k, cmd):
    answer = ['O' for _ in range(n)] # 기존 file 목록에 대해 저장 -> O면 남아있고, X면 삭제된 파일 !
    trash = [] # 삭제한 파일의 인덱스를 저장
    bottom = n-1 # 가장 마지막 파일을 표시
    cur = int(k) # 현재 가리키는 파일의 위치를 표시 
    
    for c in cmd:
        if c[0] == "U":
            command, x = c.split()
            cnt = 1
            while cnt <= int(x): # 위로 n칸 이동하기 
                cur = (cur-1)%n
                if answer[cur] == "O":
                    cnt += 1 # 빈칸에 대해서만 카운트
            
        elif c[0] == "D":
            command, x = c.split()
            cnt = 1
            while cnt <= int(x): # 아래로 n칸 이동하기
                cur = (cur+1)%n
                if answer[cur] == "O":
                    cnt += 1

        elif c[0] == "C":
            answer[cur] = 'X' # 삭제 -> 현재 가리키는 파일 x로 마크
            trash.append(cur)

            if cur == bottom:
                # 가장 아래 행이었으면
                cur = (cur-1)%n 
                while answer[cur] != 'O': # 한칸 위에꺼 가리키기
                    cur = (cur-1)%n
                bottom = cur
            else:
                cur = (cur+1)%n
                while answer[cur] != 'O': # 한칸 아래거 가리키기
                    cur = (cur+1)%n

        else:
            answer[trash[-1]] = 'O' # 제일 최근에 삭제한거 복구하기
            if bottom < trash[-1]:
                bottom = trash[-1]
            trash.pop()

    return ''.join(answer)

print(solution(8,	2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))