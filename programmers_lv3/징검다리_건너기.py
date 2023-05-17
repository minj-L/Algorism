def solution(stones, k):
    answer = 0

    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2 
        # 임의로 정한 건널 수 있는 최소한의 사람

        cnt = 0
        for s in stones:
            # 현재 징검다리 숫자가 건널 수 있는 사람 수 보다 적으면
            if s - mid <= 0:
                cnt += 1 # 사용할 수 없는 징검다리의 숫자를 늘린다
            else:
                cnt  = 0
            if cnt >= k:
                break
    
        if cnt < k:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
