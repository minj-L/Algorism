from collections import deque

computer = int(input())
pair = int(input())

# 하나의 노드에 연결된 노드가 많을 수도 있으니 0이 아닌 []를 늘려야 했다.
#node = [0 for _ in range(computer + 1)]

node = [[] for _ in range(computer + 1)]
visited = [0] * (computer + 1)

for _ in range(pair):
    p1, p2 = map(int, input().split())
    node[p1] += [p2]
    node[p2] += [p1]

visited[1] = 1
Q = deque([1])

while Q:
    current_node = Q.popleft()
    for i in node[current_node]:
        if visited[i] == 0:
            Q.append(i)
            visited[i] = 1
print(sum(visited) - 1) # 1은 감염시킨 컴퓨터니까 제외
