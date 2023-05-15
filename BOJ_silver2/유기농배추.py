#인접한 배추 구역이 몇개가 있는지를 구해야 한다.

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # 상 하 좌 우

t = int(input())

# 1인 구역을 모두 0으로 바꾸는 작업
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            #모두 0이 되어 더 이상 돌 수 있는 곳이 없으면 bfs를 멈춘다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    # 가로, 세로, 심긴 배추 개수
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    # 배추 심긴 위치 저장
    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
