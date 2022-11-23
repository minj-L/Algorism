def solution(n, results):
    answer = 0
    board = [[None for _ in range(n)] for _ in range(n)]

    #Adjacency Matrix
    for a,b in results:
        board[a-1][b-1] = 1 #이긴 사람
        board[b-1][a-1] = -1 #진 사람
    
    # 플로이드 - 워셜 알고리즘
    for i in range(n):
        for j in range(n):
            for k in range(n):
                #연결되지 않거나 연결상태가 이상한 노드는 연결하지 않고 건너 뛴다.
                if board[j][i] == None:
                    continue
                # if j -> i 가 False이고 i -> k 가 False라면
                if board[j][i] == board[i][k]:
                    board[j][k] = board[j][i] # j -> k도 False 이다.
                    board[k][j] = not board[j][i] # k -> j에는 j -> i의 결과에 반대 되는 값을 넣어준다.
    answer = 0
    for i in range(n):
        #만약 자기 자신이 아닌 곳에 None을 가지고 있다면 카운트 하지 않는다.
        if None in board[i][:i] + board[i][i+1:]: #i번째 요소에서 i-1까지를 보여달라
            continue
        answer += 1
    return answer
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

    
