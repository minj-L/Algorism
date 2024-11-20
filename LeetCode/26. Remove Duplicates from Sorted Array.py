# 딕셔너리로 풀어버리고 싶다 키값만 가져다가 세면 안돼?
def solution(nums):
    # answer = 0
    # dic = {}

    # for i in nums:
    #     if i in dic:
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1

    # for i in dic:
    #     answer += 1

    # return int(answer)

    # 기존 리스트의 개수를 유지하는 것이 관건이었다.
    if len(nums) == 0:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1



print(solution([0,0,1,1,1,2,2,3,3,4]))