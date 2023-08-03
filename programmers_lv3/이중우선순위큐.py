import heapq

def solution(operations):
    # 힙에 넣을 item을 저장하는 배열
    heap = []
    answer = []

    for o in operations:
        split_o = o.split()
        #print(o.split(' '))
        if split_o[0] == "I":
            heapq.heappush(heap, split_o[1])
        else:
            if split_o[0] == "D" and split_o[1] == "-1":
                heapq.heappop(heap)
            elif split_o[0] == "D" and split_o[1] == "1":
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))


# import heapq

# def solution(operations):
#     heap = []
#     answer = []

#     for i in operations:
#         op = i.split()
#         if op[0] == "I":
#             heapq.heappush(heap, int(op[1]))
#         else:
#             if len(heap) == 0:
#                 pass
#             elif op[1] == "-1":
#                 heapq.heappop(heap)
#             else:
#                 heap = heapq.nlargest(len(heap), heap)[1:]
#                 heapq.heapify(heap)

#     if heap:
#         answer.append(max(heap))
#         answer.append(min(heap))
#     else:
#         answer.append(0)
#         answer.append(0)
#     return answer