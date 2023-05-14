# from collections import deque

# deque = deque()

# def push_front(x):
#     return deque.appendleft(x)

# def push_back(x):
#     return deque.append(x)

# def pop_front():
#     if not deque:
#         return -1
#     else:
#         left = deque.popleft()
#         return left

# def pop_back():
#     if not deque:
#         return -1
#     else:
#         back = deque.pop()
#         return back
    
# def size():
#     return len(deque)

# def empty():
#     if not deque:
#         return 1
#     else:
#         return 0

# def front():
#     if not deque:
#         return -1
#     else:
#         left = deque[0]
#         return left
    
# def back():
#     if not deque:
#         return -1
#     else:
#         back = deque[-1]
#         return back
    
# n = int(input())
# command = []
# for _ in range(n):
#     cmd, num = input.split()
#     command.append([cmd, num])

# for c in command:
#     if c[0] == 'push_back':
#         push_back(c[1])
#     if c[0] == 'push_front':
#         push_front(c[1])
#     if c[0] == 'front':
#         front()
#     if c[0] == 'back':
#         back()
#     if c[0] == 'size':
#         size()
#     if c[0] == 'empty':
#         empty()
#     if c[0] == 'pop_front':
#         pop_front()
#     if c[0] == 'pop_back':
#         pop_back()


from collections import deque
import sys

d = deque()
n = int(input())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push_front":
        d.appendleft(command[1])
    elif command[0] == "push_back":
        d.append(command[1])
    elif command[0] == "pop_front":
        if d:
            print(d[0])    
            d.popleft()
        else:
            print("-1")
    elif command[0] == "pop_back":
        if d:
            print(d[len(d) - 1])    
            d.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif command[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")
