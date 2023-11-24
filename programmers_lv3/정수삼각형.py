def solution(triangle):
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0: # 숫자가 가장 왼쪽에 있을 때
                triangle[i][j] += triangle[i-1][j]
            elif j==i: # 숫자가 가장 오른쪽에 있을 때
                triangle[i][j] += triangle[i-1][-1]
            else: # 가운데 부분에 있을 때
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])