def solution(A):
    for i in A:
        cnt = A.count(i)
        if cnt == 1:
            return i
print(solution([9,3,9,3,9,7,9]))

#시간복잡도 문제로 미해결

def solution(A):
    if len(A) == 1:
        return A[0]
    
    A = sorted(A) #본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환
    for i in range (0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        if A[i] != A[i+1]:
            return A[i]
#시간 복잡도 O(N) or O(N*log(N))으로 줄임 참고한 블로그 있음
#https://wayhome25.github.io/algorithm/2017/04/30/OddOccurrencesInArray/
