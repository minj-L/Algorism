import heapq


def maxProduct(nums):
    heap =[]
    max_heap = []

    for s in nums:
        heapq.heappush(heap, (-s, s))

    while heap:
        max_heap.append(heapq.heappop(heap)[1])
            
    first_max = max_heap[0] - 1
    second_max = max_heap[1] - 1

    return first_max * second_max