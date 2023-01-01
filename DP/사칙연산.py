def solution(arr):
    min_Max = [0, 0]
    sum_res = 0 #더하기 부호가 있는 수를 다 더한 결과 값 저장
    for i in range(len(arr) - 1, -1, -1): #뒤에서 부터 연산 부호를 찾아나간다.
        if arr[i] == '+':
            continue
        elif arr[i] == '-':
            miN, maX = min_Max
            #min 값 구하기
            min_Max[0] = min(-(sum_res + maX), -sum_res+miN)
            # -가 붙는 값
            minus_v = int(arr[i+1])
            #max 값 구하기
            min_Max[1] = max(-(sum_res+miN), -minus_v+(sum_res-minus_v)+maX)
            sum_res = 0
        elif int(arr[i]) >= 0: #부호가 아니라 숫자가 들어간 경우
            sum_res += int(arr[i])
    min_Max[1] += sum_res
    return min_Max[1]
#
