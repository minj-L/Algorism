def solution(A, K):
    if A == []:
        return [] 
    for _ in range(K):
        temp = A.pop()
        A.insert(0, temp)
    return A

print(solution([], 4))
