def solution(alp, cop, problems):
    answer = 0
    times = 0
    
    max_alp, max_cop = 0, 0
    
    # 목표하는 코딩 능력치를 찾아준다.
    for i in range(len(problems)):
        max_alp = max(problems[i][0], max_alp)
        max_cop = max(problems[i][1], max_cop)
        
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    
    max_cost = 100 * (max_alp + max_cop)
    dp = [[max_cost + 1 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
            
    dp[alp][cop] = 0
    # dp에 채울수 있는 알고력과 코딩력을 저장
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
    
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 현재 alp 값이 요구되는 alp_req 값 보다 크거나 값으면
                if i >= alp_req and j >= cop_req:
                    # 다음 문제를 풀이하여 알고력과 코딩력을 늘릴 수 있게 해준다.
                    # 목표까지 도달하는데 걸리는 최단시간을 구하라 했으므로 min값을 저장
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    
    #print(dp)
    # dp의 끝이 목표하는 코딩능력으로 모든 문제를 풀수있는 최단시간이 된다.
    return dp[-1][-1]
