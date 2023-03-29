def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0] = 1
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for i in range(len(edges)):
            parent_node = edges[i][0]
            child_node = edges[i][1]
            animal = info[child_node]
            if visited[parent_node] and not visited[child_node]:
                visited[child_node] = 1
                dfs(sheep + (animal==0), wolf+(animal==1))
                visited[child_node] = 0
    dfs(1, 0)
    print(answer)
    return max(answer)
