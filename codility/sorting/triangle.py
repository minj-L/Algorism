def solution(A):
    A = sorted(A)

    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0
print(solution([10, 2, 5, 1, 8, 20]))

#https://datacodingschool.tistory.com/34
#댑악,,이렇게 생각하면 되는 구나
