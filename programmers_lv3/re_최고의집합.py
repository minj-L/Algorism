def solution(n, s):
    # 최고의 집합이 나올 수 없는 경우는 무엇알까?
    result = []

    if n > s:
        result.append([-1])

    que, rem = divmod(s, n)

    result = [que] * n

    for i in range(rem):
        result[i] += 1

    return sorted(result)
print(solution(2, 9))