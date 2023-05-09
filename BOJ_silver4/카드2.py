# def solution(n):
#     answer = 0

#     card_list = []

#     for i in range(1, n+1):
#         card_list.append(i)

#     for _ in range(n-1):
#         card_list.pop(0)
#         for j in range(len(card_list)-1):
#             tmp = card_list[j + 1]
#             card_list[j + 1] = card_list[j]
#             card_list[j] = tmp

#     #print(card_list)
#     return card_list[0]

# print(solution(6))
# 시간초과 뜸

# new one
from collections import deque

n = int(input())
deque = deque([i for i in range(1, n+1)])

while (len(deque) > 1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])
