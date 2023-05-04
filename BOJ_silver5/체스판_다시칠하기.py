n, m = map(int, input().split())
chess = []
result = []

for _ in range(n):
    chess.append(input())

for i in range(n-7):
        for j in range(m-7):
            draw1 = 0 # w로 시작할 경우 바뀐 체스판의 개수를 세기 위함
            draw2 = 0 # b로 시작할 경우 바뀐 체스판의 개수를 세기 위함
            for a in range(i, i+8):
                for b in range(j, j+8):
                    if (a + b) % 2 == 0: # 현재 행과 열의 합이 짝수 일 경우 시작점의 색깔과 같아야 한다.
                        if chess[a][b] != 'B':
                            draw1 += 1
                        if chess[a][b] != 'W':
                            draw2 += 1
                    else: # 현재 행과 열의 합이 홀수 일 경우 시작점의 색깔과 달라야 한다.
                        if chess[a][b] != 'W':
                            draw1 += 1
                        if chess[a][b] != 'B':
                            draw2 += 1
            result.append(draw1)
            result.append(draw2)
    
print(min(result))
