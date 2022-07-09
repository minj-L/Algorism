def solution (X, Y, D):
    cnt = 0
    while X <= Y:
        X += D
        cnt += 1
    return cnt
print(solution(10, 85, 30))

#오류 많음 11% 나옴

def solution (X, Y, D):
    des = Y - X # 개구리가 목표 지점 까지 가기위해 뛰어야 하는 거리
    Q = des // D
    R = des % D

    if R == 0:
        return Q
    elif R < D:
        return Q + 1

print(solution(10, 85, 30))
