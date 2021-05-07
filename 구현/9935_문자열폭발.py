import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
last_bomb = bomb[-1]

stack = []
for s in string:
    stack.append(s)
    if s == last_bomb and "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))