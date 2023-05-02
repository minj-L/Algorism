#플로이드-와샬 : 모든 정점에서 모든 정점으로의 최단경로
def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    # 각 노드마다 부과되는 요금 저장할 곳
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

    #노드 연결 정보 저장
    for f in fares:
        node1, node2, charge = f
        graph[node1 - 1][node2 - 1] = charge
        graph[node2 - 1][node1 - 1] = charge

    for k in range(n): #모든 노드를 중간점으로 가정한다.
        for i in range(n): 
            for j in range(n):
                # 그냥 인접한 노드로 가는 것과 합승 후 어디를 거쳐서 가는 것 중
                # 더 요금이 덜 드는 값을 그래프 배열에 저장한다.
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for t in range(n):
        #출발점을 기준으로 어떤 점 T를 거쳐 a와 b로 가는 최소 비용을 탐색한다.
        temp = graph[s - 1][t] + graph[t][a-1] + graph[t][b-1]
        answer = min(temp, answer)

    return answer
