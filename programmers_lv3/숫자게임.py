def solution(A, B):
    answer = -1
    
    win_count = 0
    
    A.sort(reverse = True)
    B.sort(reverse = True)

    for a in A:
        if a >= B[0]:
            continue
        else:
            win_count += 1
            del B[0]
            
    return win_count
