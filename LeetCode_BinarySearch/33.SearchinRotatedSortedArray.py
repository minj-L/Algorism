# 그냥 타겟 찾으라는거 아녀,,말을 어렵게함..
# 이게 오름차순 여부를 구별해야해서 까다로웠음 다시
# logn의 시간복잡도를 가져야 한다

def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        
        if nums[start] <= nums[mid]:
            if target >= nums[start] and target < nums[mid]:
                end = mid -1
            else:
                start = mid + 1
        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

print(search([4,5,6,7,0,1,2], 0))
