def solution(board, skill):
#     answer = []
    
#     for s in skill:
#         for i in range(s[1], s[3]+1): # 이 부분에서 2차원 배열의 원소를일일이 참조하기 때문에 시간 복잡도가 O(N*M)이 된다.
#             for j in range(s[2], s[4]+1):
#                 if s[0] == 1:
#                     board[i][j] -= s[5]
#                 elif s[0] == 2:
#                     board[i][j] += s[5]  
#     #print(board)
#     for one_line in board:
#         for ol in one_line:
#             if ol > 0:
#                 answer.append(ol)
                
#     #print(len(answer))
#     return len(answer)


    answer = 0
    #누적합을 만들 빈 배열
    tmp = [[0 for j in range(len(board[0])+1)] for i in range(len(board) + 1)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 2:
            d = -d
        tmp[r1][c1] -= d
        tmp[r1][c2+1] += d
        tmp[r2+1][c1] += d
        tmp[r2+1][c2+1] -= d
    
    # 행 기준 누적합
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1] += tmp[i][j]
    
    # 열 기준 누적합
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i+1][j] += tmp[i][j] #마지막에 한번 누적합을 계산 O(1)의 시간복잡도를 가진다.
    
    # 기존의 배열과 합침
    for i in range(len(board)):
        for j in range(len(board[0])):
            #만약 이 더한 값이 0 보다 크면 answer 증가
            if board[i][j] + tmp[i][j] > 0:
                answer += 1
    
    return answer
