# 최악최악 풀이방법이 떠오르지 않아 답지 보고 풀이함

def solution(triangle):

    for line in range(1, len(triangle)):
        for idx in range(line + 1):
            if idx == 0:
                triangle[line][idx] += triangle[line-1][idx]
            elif idx == line:
                triangle[line][idx] += triangle[line-1][-1]
            else:
                triangle[line][idx] += max(triangle[line-1][idx-1], triangle[line-1][idx])

    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
