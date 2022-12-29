def solution(N, number):
    answer = 0
    S = [0, {N}] #조합으로 나올 수 있는 숫자들을 저장하는 곳
    if N == number:
        return 1
    for i in range(2, 9): #N이 8까지 이므로 8까지 for문을 돌려 조합을 찾는다
        case_set = []
        basic_num = int(str(N) * i)
        case_set.append(basic_num) #각 i별 조합 결과를 저장ㅇ한다
        for i_half in range(1, i//2+1):
            for x in S[i_half]:
                for y in S[i-i_half]:
                    case_set.append(x+y)
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y != 0:
                        case_set.append(x/y)
                    if x != 0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            S.append(case_set)
    return -1
