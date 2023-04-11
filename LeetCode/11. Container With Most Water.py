class Solution:
    def maxArea(self, height: List[int]) -> int:

        # res = []
        # for i in range(0, len(height)-1): # height 0 ~ 7
        #     for j in range(i+1, len(height)): # height i+1 ~ 8
        #         r_height = min(height[i], height[j])
        #         area = abs(i - j) * r_height # (1-0) * height[0] == 1
        #         res.append(area)
        
        # return max(res)
        # Time Limit Exceeded

        
        # if len(height) == 2:
        #     return max(height) * 1  
        # else:
        #     if count(max(height)) >= 2:

        #     first_max_index = height.index(max(height))

        #     remove_set = {max(height)}
        #     new_height = [i for i in height if i not in remove_set]
            
        #     seconde_max = max(new_height)
        #     seconde_max_index = height.index(max(new_height))

        #     area = seconde_max * abs(first_max_index-seconde_max_index)
        #     return area
        # [4,3,2,1,4] testcase error

        # 투 포인터를 사용해야 했다

        left = 0
        right = len(height) - 1
        max_area = 0
        while (right - left > 0): #left가 짧다고 상정
            max_area = max(max_area,(right-left)*min(height[left],height[right]))

            if height[left] >= height[right]: #그래서 left가 right보다 커지면 right를 옮기는 것이다.
                right -= 1
            else:
                left += 1 #짧은 포인터를 옮겨야 그 다음 컨테이너의 크기가 커질 수 있기 때문
        return max_area
