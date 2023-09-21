# def add(command, number):
#     if command == 'add':
#         S.add(number) 

# def check(command, number):
#     if command == 'check': 
#         if number in S:
#             print(1)
#         else:
#             print(0)

# def remove(command, number):
#     if command == 'remove':
#         S.discard(number)

# def toggle(command, number):
#     if command == 'toggle':
#         if number in S:
#             S.discard(number)
#         else:
#             S.discard(number)

# def all(command):
#     if command == 'all':
#         S = {i for i in range(1, 21)}
#     else:
#         s = set()
#     continue

# def empty(command):
#     if command == 'empty':
#         S.clear()
import sys

S = set()

num = int(input())

for _ in range(num):
    #command, number = map(str, input().split(" "))
    
    tmp = sys.stdin.readline().strip.split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            S = set({i for i in range(1, 21)})
        else:
            S = set()
        continue

    command, number = tmp[0], tmp[1]
    number = int(number)

    if command == 'add':
        S.add(number)
    elif command == 'check':
        print(1 if num in S else 0)
    elif command == 'remove':
        S.discard(number)
    elif command == 'toggle':
        if number in S:
            S.discard(number)
        else:
            S.add(number)