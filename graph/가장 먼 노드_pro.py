from collections import deque

def solution(n, edge):
    answer = 0
    visited = [0] * (n+1) # 각 노드의 방문정보를 저장하기 위함
    edge.sort() # 노드 1부터의 연결 정보를 정렬
    print(edge)
    graph = [[] for i in range(n+1)] #각 노드에 연결된 노드 정보들을 저장하기 위함
    queue = deque()

    # 양방향 노드의 연결정보를 다음과 같은 방법으로 저장
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    print(graph)

    # 큐에다 노드를 하나씩 넣음
    queue.append(1)
    # 해당 노드에 방문 했음을 1씩 증가시키며 확인해야 하기에 
    # 출발 노드인 1번 노드를 1로 초기화
    visited[1] = 1

    while queue:
        now = queue.popleft()
        # 각 노드들에 방문한 횟수를 카운트 함
        for g in graph[now]:
            if visited[g] == 0:
                queue.append(g)
                visited[g] = visited[now] + 1
    
    far_node = max(visited)
    for r in visited:
        if r == far_node:
            answer +=1
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
