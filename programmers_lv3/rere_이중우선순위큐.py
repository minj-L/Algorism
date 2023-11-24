import heapq

def solution(operations):

    queue = []
    answer = []

    for o in operations:
        o_split = o.split(" ")
        
        if o_split[0] == 'I':
            heapq.heappush(queue, int(o_split[1]))
        else:
            if len(queue) == 0:
                pass
            elif o_split[0] == 'D' and o_split[1] == '-1':
                heapq.heappop(queue)
            elif o_split[0] == 'D' and o_split[1] == '1':
                queue = heapq.nlargest(len(queue), queue)[1:]
                heapq.heapify(queue)
    if queue:
        answer.append(max(queue))
        answer.append(min(queue))
    else:
        answer.append(0)
        answer.append(0)
    return answer
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))