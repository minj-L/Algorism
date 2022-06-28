def solution(array, commands):
    cutArray = []
    result = []
    for part2 in commands:
        i = part2[0]
        j = part2[1]
        k = part2[2]
        #print(i, j, k)
        
        for part in range(i-1, j):
            cutArray.append(array[part])
            cutArray.sort()
        result.append(cutArray[k-1])
        cutArray.clear()
    return result
    
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
