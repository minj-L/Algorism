def solution(s1, s2):
    s3 = list(set(s1) - set(s2))
    return s3
print(solution([4, 99, 2, 6, 7, 13, 88, 76], [6, 88, 13, 4, 99, 2, 7]))
#순서보존이 안된다는 단점 문제에서는 순서 상관 없다고 하긴 함

s = set(s2)
s3 = [x for x in s1 if x not in s]
#x부터 s1까지 돌아서 만약 x가 s에 없다면 그걸 x에 넣어라
#얘는 순서 보존이 됨
print(s3)
