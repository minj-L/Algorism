# n/2개의 폰켓몬을 고르고 
# n/2개 내에서 고를 수 있는 폰켓몬의 종류를 최대한 다양하게 만들고 싶다.
def solution(nums):
    no_duplicated_len = len(set(nums))
    you_can_get = int(len(nums) / 2)

    if you_can_get > no_duplicated_len:
        return no_duplicated_len
    else:
        return you_can_get
print(solution([3,3,3,2,2,4]))