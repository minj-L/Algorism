def solution(A):
    a = []
    for z in range(len(A)):
        a.append(z)

    res = 0
    comb = list(combinations(a, 2))
    #print(comb)

    b = []

    for i in comb:
        #print(i[1])
        for j in range(i[0], i[1]+1):
            # A[j] += A[j+1] // ((i[1] - i[0])+1)
            #print(j)
            res+=A[j]
            res2 = round((res / ((i[1] - i[0])+1)),2)
        #print(res2)
        b.append(res2)
        res = 0
    return min(comb[b.index(min(b))])

print(solution([4, 2, 2, 5, 1, 5, 8]))

#정답률 50% 시간복잡도 O(N ** 3) 처음본다,,
