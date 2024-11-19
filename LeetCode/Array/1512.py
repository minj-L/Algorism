class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_cnt_save = []
        result_save = []

        drop_distinct = list(set(nums))
        for dist in drop_distinct:
            nums_cnt = nums.count(dist)
            if nums_cnt > 1:
                nums_cnt_save.append(nums_cnt)
        
        for nums in nums_cnt_save:
            res = (nums * (nums-1)) // 2
            result_save.append(res)

        if not nums_cnt_save:
            result = 0
        else:
            result = sum(result_save)

        return result
