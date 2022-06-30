def solution(progresses, speeds):
    rele = [] #결과 저장하는 배열
    count = 0
    day = 0

    for _ in range(len(progresses)):
        top = progresses.pop(0)
        top2 = speeds.pop(0)
        while True:
            if (top + day * top2) >= 100:
                count += 1
                print(count)
                break
            else :
                if count > 0:
                    rele.append(count)
                    count = 0
                day += 1
    rele.append(count)

    return rele

print(solution([93, 30, 55], [1, 30, 5]))
