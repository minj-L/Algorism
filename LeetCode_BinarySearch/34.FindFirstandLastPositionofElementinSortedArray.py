# def solution(nums, target):
#     start = 0
#     end = len(nums) - 1

#     res = []
#     while start <= end:
#         mid = (start + end) // 2

#         if nums[mid] <= target:
#             if nums[mid] == target:
#                 res.append(mid)
#             else:
#                 start = mid + 1
#         else:
#             if mid < start or mid > end:
#                 res.append(-1)
#             else:
#                 end = mid - 1
#     return res

# print(solution([5,7,7,8,8,10], 8))

def solution(nums, target):
    start = 0
    end = len(nums) - 1

    answer = [-1, -1]
    while start <= end:
        if answer[0] != -1 and answer[1] != -1:
            break
        if target > nums[start]:
            start += 1
        elif target == nums[start]:
            answer[0] = start
        
        if target < nums[end]:
            end -= 1
        elif target == nums[end]:
            answer[1] = end
    return answer
