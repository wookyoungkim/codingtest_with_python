import sys 
import itertools

input = sys.stdin.readline
n = int(input())
board = []
teacher = []
student = []
space = []

for i in range(n):
  tmp = list(input().split())
  for j in range(n):
    if tmp[j] == 'T':
      teacher.append((i,j))
    elif tmp[j] == 'S':
      student.append((i,j))
    else:
      space.append((i,j))
  board.append(tmp)
  
def check_success():
  for x,y in teacher:
    i,j = x-1,y
    oflag = 0
    #상
    while i>=0:
      if board[i][j] == 'O':
        oflag = 1
      if board[i][j] == 'S' and oflag != 1:
        return False
      i -= 1
    #하
    i,j = x+1,y
    oflag = 0
    while i<n:
      if board[i][j] == 'O':
        oflag = 1
      if board[i][j] == 'S' and oflag != 1:
        return False
      i += 1
    #좌
    i,j = x,y-1  
    oflag = 0
    while j>=0:
      if board[i][j] == 'O':
        oflag = 1
      if board[i][j] == 'S' and oflag != 1:
        return False
      j -= 1
    #우
    i,j = x,y+1  
    oflag = 0
    while j<n:
      if board[i][j] == 'O':
        oflag = 1
      if board[i][j] == 'S' and oflag != 1:
        return False
      j += 1
  return True

def solution():
  for objects in itertools.combinations(space, 3):
      #print(list(objects))
      for x,y in objects:
        board[x][y] = 'O'
      if check_success():
        print("YES")
        return
      for x,y in objects:
        board[x][y] = 'X'
  print("NO")
  
solution()