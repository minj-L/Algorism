def solution(n):
    answer = 0
    sugar_bag = 0
    
    # sugar += n // 5
    # if (n % 5) % 3 == 0:
    #     sugar += (n % 5) // 3
    # elif (n % 5) % 3 != 0:

    while n >= 0:
        if n % 5 == 0:
            sugar_bag += n // 5
            return sugar_bag
        n -= 3
        sugar_bag += 1
    else:
        return -1

print(solution(7))
