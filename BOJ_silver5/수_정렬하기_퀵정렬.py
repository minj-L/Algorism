#퀵 정렬 최악일 때 O(n^2) 최선일 때 O(nlongn)
def solution(arr, start, end):
    if start >= end:
        return
    # 첫 번째 원소를 피벗으로 설정한다.
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        #피벗보다 큰 데이터를 찾기 전까지 왼쪽에서 +1을 해준다.
        #즉 arr[left] > arr[pivot]이 되는 순간 left += 1 하는 것을 멈추는 것이다.
        #피벗보다 큰 데이터라면 앞이 아니라 뒤에 가야 하니까 그냥 놔두고 자리를 바꾸도록 하는 것이다
        #근데 피벗보다 큰 데이터가 아니면 앞에 있어도 되니까 left += 1을 하는 것이다.
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        #피벗보다 작은 데이터를 찾기 전까지 -1을 해준다.
        #arr[right] < arr[pivot] 되는 순간 right -= 1 하는 것을 멈춘다.
        #피벗보다 작은 데이터라면 뒤가 아니라 앞에 가야 하니까 그냥 놔두고 자리를 바꾸도록 하는 것이다
        #근데 피벗보다 작은 데이터가 아니면 뒤에 있어도 되니까 right-=1 을 하는 것이다.
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 위 과정을 거치고 left가 right를 역전했다는 것은 피봇이 right 인덱스에 있는 값보다는 뒤로 가야 한다는 의미이다.
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    solution(arr, 0, right -1) #왼쪽 파티션
    solution(arr, right + 1, end) #오른쪽 파티션

    # small = []
    # big = []
    # for i in range(len(number)):
    #     if number[i] < pivot:
    #         small.append(number[i])
    #     elif number[i] > pivot:
    #         big.append(number[i])
    #     else:
    #         continue
    # print(small)
    # print(big)
    return arr

arr = [3, 4, 5, 1, 2]
print(solution(arr, 0, len(arr)-1))
