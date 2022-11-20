def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n #심사를 받는 시간 범위
    while left <= right:
        mid = (left + right) // 2 #모든 심사관에게 주어진 시간 30.~~(중간 값)
        people = 0 #모든 심사관들이 mid분 동안 심사한 사람의 수(기준/타겟 값)
        for time in times:
            people += mid // time
            #모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문 out
            if people >= n:
                break
        
        #심사할 수 있는 사람이 심사 받아야 할 사람 보다 많거나 같으면
        if people >= n:
            answer = mid
            right = mid -1 #mid기준 왼쪽 범위를 탐색
        #심사할 수 있는 사람이 심사 받아야 할 사람 보다 적으면
        elif people < n:
            left = mid + 1 #mid기준 오른쪽 범위를 탐색
    return answer
print(solution(1, [7, 10]))
