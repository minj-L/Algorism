t = int(input())
for _ in range(t):
    n = int(input())
    zero, one = 1, 0 # 일단 시작 0 하나 있으니까
    for i in range(n):
        zero, one = one, zero + one
    print(zero, one)
# hint! 각 숫자가 가지는 0과 1의 규칙을 찾아라 
