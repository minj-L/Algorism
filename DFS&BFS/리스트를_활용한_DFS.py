graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)

def dfs(graph, start_node):
    # need_visited 방문이 필요한 노드를 저장하는 리스트
    # visited 방문한 노드를 저장하는 리스트
    need_visited, visited = list(), list()
    # 가장 기본 적인 것은 항상 방문이 필요한 리스트와 방문한 리스트들을 저장하는 곳을 만들어 둔다.

    need_visited.append(start_node)

    # 방문해야 할 노드가 있다면
    while need_visited:
        node = need_visited.pop() #pop은 리스트에서 가장 끝에 있는 값을 꺼내온다.

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node]) #graph[node]의 값을 방문이 필요한 리스트에 추가
            # extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣는다
            # https://m.blog.naver.com/wideeyed/221541104629 참고
            print(need_visited)
    return visited #노드를 방문한 순서를 저장한 배열이 반환 됨
print(dfs(graph, 'A'))

#다만 list에서 pop을 활용하면 성능면에서 떨어지는 단점이 있어요. 
