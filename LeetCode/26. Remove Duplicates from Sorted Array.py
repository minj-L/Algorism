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

    if len(nums) == 0:
        return 0
    
    for i in range(1, len(nums)):
        


print(solution([0,0,1,1,1,2,2,3,3,4]))