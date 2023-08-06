import heapq

def solution(operations):
    # 힙에 넣을 item을 저장하는 배열
    heap = []
    answer = []

    for o in operations:
        split_o = o.split()
        #print(o.split(' '))
        if split_o[0] == "I":
            heapq.heappush(heap, int(split_o[1])) # 문자로 하면 아스키로 계산되니 조심
        else:
            if len(heap) == 0:
                pass
            elif split_o[0] == "D" and split_o[1] == "-1":
                heapq.heappop(heap)
            elif split_o[0] == "D" and split_o[1] == "1":
                #print(heap)
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
    return answer


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
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))