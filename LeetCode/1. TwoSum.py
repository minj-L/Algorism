# 1 Try
from itertools import combinations

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        comb = list(combinations(nums, 2))
        for i in comb:
            if sum(i) == target:
               for j in i:
                   id = nums.index(j)
                   print(id)
                   answer.append(id)
        return answer
      
# 2 Try
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    answer.append(i)
                    answer.append(j)
                    break
        return answer
#
