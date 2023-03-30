class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = 0
        
        new_nums = nums1 + nums2
        new_nums.sort()
        print(new_nums)

        if len(new_nums) == 1:
            return new_nums[0]
        if len(new_nums) % 2 == 0:
            front_num = int(len(new_nums) / 2 - 1)   
            back_num = int(len(new_nums) / 2)
            print(new_nums[front_num])

            res = (new_nums[front_num] + new_nums[back_num]) / 2 
            return round(res, 1)
        else:
            res_num = int((len(new_nums) + 1) / 2)
        return new_nums[res_num-1]
      
  # 배열 내의 원소들이 출력될 수 있게 하는 것을 고려하지 않음->배열 전체 길이의 값으로 계산해서 출력해가지고 [0,0,0,0] 같은 값은 답이 이상하게 나옴
  # 배열 내 원소가 1개일 경우 
