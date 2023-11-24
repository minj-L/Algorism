def solution(nums):
    answer = 0

    you_can_get = len(nums) // 2

    #nums 중복 제거해서 센 수가 n/2 보다 더 크면, n/2를 return
    set_num = set(nums)
    set_num_len = len(set_num)

    if set_num_len > you_can_get:
        return you_can_get
    elif set_num_len < you_can_get:
        return set_num_len
    else:
        return set_num_len

print(solution([3,3,3,2,2,4]))