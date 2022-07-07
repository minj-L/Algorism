def solution (X, Y, D):
    cnt = 0
    while X <= Y:
        X += D
        cnt += 1
    return cnt
print(solution(10, 85, 30))

#오류 많음 11% 나옴
