def solution(triangle):
    answer = 0

    for line in range(1, len(triangle)):
        for i in range(line + 1):
            if i == 0:
                triangle[line][i] += triangle[line - 1][i]
            elif i == line:
                triangle[line][i] += triangle[line - 1][-1]
            else:
                triangle[line][i] += max(triangle[line-1][i-1], triangle[line-1][i])

    return max(triangle[-1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))