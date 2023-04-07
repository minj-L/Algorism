def solution(sizes):
    
    tmp = 0
    new_c, new_r = [], []
    for c, r in sizes:
        if r > c:
            tmp = c
            c = r
            r = tmp
        new_c.append(c)
        new_r.append(r)
    
    answer = max(new_c) * max(new_r)
    return answer
#
