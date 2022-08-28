import heapq

def solution(operations):
    heap = []
    answer = []

    for i in operations:
        op = i.split()
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        else:
            if len(heap) == 0:
                pass
            elif op[1] == "-1":
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer
