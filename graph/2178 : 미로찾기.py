from collections import deque

N, M = map(int, input().split())

graph = [] #미로가 저장될 그래프

# 그래프에 미로를 표시
for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치를 확인
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            #벽을 만남!
            if graph[nx][ny] == 0:
                continue

            #벽이 아니므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]
print(bfs(0,0))
