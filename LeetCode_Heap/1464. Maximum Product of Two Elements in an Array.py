import heapq


def maxProduct(nums):
    # heap =[]
    # max_heap = []

    # for s in nums:
    #     heapq.heappush(heap, (-s, s))

    # while heap:
    #     max_heap.append(heapq.heappop(heap)[1])
            
    # first_max = max_heap[0] - 1
    # second_max = max_heap[1] - 1

    # return first_max * second_max

    first, second = 0, 0
        
    for number in nums:
            
        if number > first:
            # update first largest and second largest
            first, second = number, first
                
        elif number > second:
            # update second largest
            second = number
        
        print(first, second)

    return (first - 1) * (second - 1)

print(maxProduct([3,4,5,2]))