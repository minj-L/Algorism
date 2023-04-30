import sys
N = int(sys.stdin.readline())

stack = []

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    
    if command[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    if command[0] == 'size':
      print(len(stack))
    
    if command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    
    if command[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
