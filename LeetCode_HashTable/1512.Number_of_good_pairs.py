class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # nums_len = len(nums)
        # good_pairs = 0

        # for i in range(nums_len - 1):
        #     for j in range(1, nums_len):
        #         if (i < j) and (nums[i] == nums[j]):
        #             good_pairs += 1
        # return good_pairs

        num, repeat = 0, {}

        for v in nums:

            if v in repeat:
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]
                repeat[v] += 1
            else:
                repeat[v] = 1
            print(num)
            print(repeat)
        return num