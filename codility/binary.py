def solution (N):
    n = format(N, 'b')

    length = []
    only_0 = n.strip('0').strip('1').split('1')

    for i in only_0:
        length.append(len(i))
    return max(length)

print(solution(19 and 42))
