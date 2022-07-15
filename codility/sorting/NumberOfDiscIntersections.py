def solution(A):
    disc = []

    for i, v in enumerate(A):
        disc.append((i-v, -1))
        disc.append((i+v, 1))

    disc = sorted(disc)
    t = 0
    r = 0

    for d in disc:
        if d[1] == 1:
            t -= 1 
        else :
            r += t
            t += 1

    return r if r <= 10000000 else -1
    
    #https://smecsm.tistory.com/220
