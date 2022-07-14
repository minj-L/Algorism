def solution(S, P, Q):
    res = []
    res2 = []

    for i in range(len(S)):
        new_A = S.replace("A", "1")
        new_C = new_A.replace("C", "2")
        new_G = new_C.replace("G", "3")
        new_T = new_G.replace("T", "4")

    #print(new_T)

    for i in range(len(P)):
        for j in range(P[i], Q[i]+1):
            res.append(new_T[j])
        #print(res)
        mini = min(res)
        res2.append(int(mini))
        res.clear()
    return res2
print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
# 62% 나옴!! 나름 높게 나와서 ㅎㅎ
