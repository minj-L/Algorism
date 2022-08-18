def solution(arr):
    stack = []
    for i in range(len(arr)):
        if i == 0:
            stack.append(arr[i])
        elif arr[i] != arr[i-1]:
            stack.append(arr[i])
    return stack
