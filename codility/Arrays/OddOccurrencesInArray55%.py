def solution(A):
    for i in A:
        cnt = A.count(i)
        if cnt == 1:
            return i
print(solution([9,3,9,3,9,7,9]))

#시간복잡도 문제로 미해결
