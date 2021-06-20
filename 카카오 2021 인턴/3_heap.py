from collections import deque


class Node:
    def __init__(self): # double linked list로
        self.prev_node = None
        self.next_node = None


def solution(n, k, cmd):
    stack = deque() # 삭제 목록 저장.
    archive = deque() # archive에는 초기 파일의 순서 저장하기
    
    initial_node = Node()
    archive.append(initial_node)
    prev_node = initial_node
    
    # 1. linked list로 파일 쭉 연결해주기
    for index in range(1, n):
        generated_node = Node()
        prev_node.next_node = generated_node
        generated_node.prev_node = prev_node
        archive.append(generated_node)
        prev_node = generated_node
    
    # 2. 맨 처음 선택한 파일 찾기
    current_node = initial_node
    for _ in range(k):
        current_node = current_node.next_node
    
    # 3. cmd 따라가면서 수행
    for c in cmd:
        # 3.1 up
        if c[0] == "U":
            command, v = c.split(" ")
            for _ in range(v):
                current_node = current_node.prev_node
        # 3.2 down
        elif c[0] == "D":
            command, v = c.split(" ")
            for _ in range(v):
                current_node = current_node.next_node
        # 3.3 삭제
        elif command == "C":
            stack.append(current_node)
            # 맨 마지막 파일이 아니면
            if current_node.next_node:
                # 이때 맨 처음 파일이 아니면 이전 노드와 다음 노드를 이어주기 
                if current_node.prev_node:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    current_node = current_node.next_node
                    
                # 맨 처음 파일이면? 단순히 다음 노드 가리키게
                else:
                    current_node.next_node.prev_node = None
                    current_node = current_node.next_node
                    initial_node = current_node     
            # 맨 마지막 파일이면 
            else:
                # cur이 이전 노드 가리키게
                current_node.prev_node.next_node = None
                current_node = current_node.prev_node

        # 4. 복구
        elif command == "Z":
            # 가장 최근에 삭제된 노드 불러오기
            deleted_node = stack.pop()
            previous_node = deleted_node.prev_node
            next_node = deleted_node.next_node
            
            # 삭제된 노드가 첫번째 노드인 경우의 처리
            if previous_node is None:
                initial_node.prev_node = deleted_node
                deleted_node.next_node = initial_node
                initial_node = initial_node.prev_node
                continue
            
            # 연결해주기 ! 
            previous_node.next_node, deleted_node.next_node = deleted_node, previous_node.next_node
            if deleted_node.next_node:
                deleted_node.next_node.prev_node = deleted_node
            
    # compare
    answer = []
    while archive:
        # 초기 파일 상태와 비교하면서 ox 찍어주기 
        if archive.popleft() is initial_node:
            answer.append("O")
            initial_node = initial_node.next_node
        else:
            answer.append("X")
        
    return "".join(answer)


print(solution(8,	2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))