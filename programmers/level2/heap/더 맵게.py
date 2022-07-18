import heapq

def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
        mix_cnt = 0
    while heap[0] < k:
        try:
          heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1
    return mix_cnt
#정답 https://itholic.github.io/kata-more-spicy/ 이분 보고 풀이

# def solution(scoville, K):
#     sort_sco = sorted(scoville)
#     count = 0
#     while True:
#         if min(sort_sco) < K:
#             com_sco =  sort_sco[0] + (sort_sco[1] * 2)
#             del sort_sco[0:2]
#             sort_sco.insert(0, com_sco)
#             sort_sco = sorted(sort_sco)
#             count += 1
#         else:
#             break
#     #print(sort_sco)
#     return count

# print(solution([1,2,3,9,10,12], 7))
# 정확성 효율성에서 에러남 로직은 비슷함 난 힙을 쓰지 않았음
