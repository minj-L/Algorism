t = int(input())

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)

for _ in range(t):
    n = int(input())
    print(solution(n))
