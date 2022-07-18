def solution(s1, s2):
    s3 = list(set(s1) - set(s2))
    return s3
print(solution([4, 99, 2, 6, 7, 13, 88, 76], [6, 88, 13, 4, 99, 2, 7]))
