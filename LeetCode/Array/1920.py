# my solution
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in range(0, len(nums)):
            ans.append(nums[nums[n]])
        return ans
    
# discussion
# return [num[i] for i in nums]