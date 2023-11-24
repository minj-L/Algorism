import heapq

def solution(operations):

    answer = []
    heap = []
    for o in operations:
        o_array = o.split()
        if o_array[0] == 'I':
            heapq.heappush(heap, int(o_array[1]))
        else:
            if len(heap) == 0:
                pass
            elif o_array[1] == "-1":
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:] #가장 큰 수를 빼고 배열을 출력해야 하니까!
                heapq.heapify(heap)
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))