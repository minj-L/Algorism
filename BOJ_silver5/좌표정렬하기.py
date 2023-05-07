#람다로 풀이! JAVA로도 풀어봐야지
def solution(n, arr):
    answer = sorted(arr, key=lambda x : x[1])
    return answer
print(solution(5, [[3, 4],[1,1],[1,-1],[2,2],[3,3]]))
