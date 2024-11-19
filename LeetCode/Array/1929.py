class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for n in range(0, len(nums)):
            nums.append(nums[n])
        return nums