def solution(tri):
    answer = 0
    #1. 우선 배열을 초기화 한다
    dp = [[0] * len(tri) for _ in range(len(tri))]
    dp[0][0] = tri[0][0]
    for i in range(len(tri) - 1):
        for j in range(0, len(tri) - 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + tri[i+1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + tri[i + 1][j + 1])

    return max(dp[-1])
#
