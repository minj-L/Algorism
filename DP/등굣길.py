def solution(m, n, puddles): # m=4 n=3
    puddles = [[q, p] for [p,q] in puddles] #puddle의 좌표를 거꾸로 한다.
    #2차원 리스트를 초기값은0, x길이는 m+1, y길이는 y+1로 설정한다. (4행 3열이면 0~4행 0~3열 생성)
    dp = [[0] * (m + 1) for _ in range(n+1)] #dp, dfs, bfs문제는 좌표를 초기화 한다
    dp[1][1] = 1 #점의 시작위치

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j and j == 1: continue
            if [i, j] in puddles: # 웅덩이라면
                dp[i][j] = 0 # 이후 값에 영향을 주지 않게 하기 위해 0으로 바꿔 둔다.
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007 #자신 기준으로 위쪽과 왼쪽에 있는 좌표를 더한 값을 가져온다.

    answer = dp[n][m]
    return answer
