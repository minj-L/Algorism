def solution(A, B, K):
    res = []
    for i in range(A, B+1):
        if i % K == 0:
            res.append(i)
    return len(res)
print(solution(6, 11, 2))
#O(B-A) 듣도보도 못한 시간 복잡도가 나왔다.
