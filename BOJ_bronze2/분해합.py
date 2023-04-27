def solution(n):
    # answer = 0
    # i = 0

    # while 1:
    #     i += 1
    #     answer = n - i
    #     i_list = list(map(int,str(answer)))
    #     sum_list = sum(i_list)
    #     if sum_list == i:
    #         break

    for i in range(1, n+1):
        num = sum(map(int, str(i)))
        num_sum = i + num

        if num_sum == n:
            return i
            break
        if i == n:
            return 0

print(solution(216))
