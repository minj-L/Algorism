def solution(gems):
    answer = [0, len(gems)] # 살 보석들의 범위
    gem_kind = len(set(gems)) #보석 종류
    left, right = 0, 0
    gem_dic = {gems[0] : 1}
    #print(gem_dic)
    
    while left < len(gems) and right < len(gems):
        print(len(gem_dic))
        if len(gem_dic) == gem_kind:
            if right - left < answer[1] - answer[0]: # 차이가 0이 되는 순간이 모든 보석이 1개 이상 씩 들어있는 범위
                answer = [left, right]
                print(answer)
            else:
                gem_dic[gems[left]] -= 1
                if gem_dic[gems[left]] == 0:
                    del gem_dic[gems[left]]
                left += 1
        else: # 주로 활동할 부분은 여기
            right += 1
            
            if right == len(gems): 
                break # 다 돌았으므로 멈춤
            if gems[right] in gem_dic: # right포인터 위치의 보석이 dic에 있으면
                gem_dic[gems[right]] += 1 # 딕셔너리 값 1 증가
            else:
                gem_dic[gems[right]] = 1 # 없으면 1 넣어주기
    print(gem_dic)
    return [answer[0]+1, answer[1]+1]
##
