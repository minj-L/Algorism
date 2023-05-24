from collections import deque

def solution(n, k):
    answer = []

    queue = deque()

    for i in range(1, n + 1):
        queue.append(i)

    while queue:
        for i in range(k-1):
            queue.append(queue.popleft())
        answer.append(queue.popleft())
    
    print("<", end='')
    for i in range(len(answer) - 1):
        print("%d, "%answer[i], end='')
    print(answer[-1], end='')
    print(">")
    return answer
print(solution(7, 3))
#
