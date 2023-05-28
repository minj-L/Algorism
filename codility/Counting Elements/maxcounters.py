# A=[3, 4, 4, 6, 1, 4, 4]
# N = 5
# arr = [0] * N

# for i in A:
#     if i == N + 1:
#         arr = [max(arr)] * N
#     else:
#         arr[i-1] += 1
# print(arr)

# def solution(N, A):
#     arr = [0] * N

#     for i in A:
#         if i == N + 1:
#             arr = [max(arr)] * N
#         else:
#             arr[i-1] += 1
#     return arr
# print(solution(5, [3, 4, 4, 6, 1, 4, 4]))

def solution(N,A):
    counters = [0] * N

    for m in A:
    	# 각 명령에 대해
        if m == N+1:
            max_val = max(counters)
            for i in range(1,N+1):
            #만약 N+1 이면 모든 카운터의 값을 설정한다.
                counters[i] = max_val
        else:
            counters[m] += 1
            max_val = max(max_val,counters[m])
        return counters
print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
#
