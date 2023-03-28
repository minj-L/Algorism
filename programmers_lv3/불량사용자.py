from itertools import permutations

def check(unit, ban):
    for i in range(len(unit)): # unit은 banned_id 수만큼의 조합
        if len(unit[i]) != len(ban[i]):
            return False
        for j in range(len(unit[i])):
            if unit[i][j] != ban[i][j] and ban[i][j] != "*": # ban이 다 *이면 True로 통과 될수 있게 ban[i][j] != "*" 규칙 추가
                return False
    #print(unit)
    return True

def solution(user_id, banned_id):
    answer = []
#     id_dic = {}
#     for user in user_id:
#         id_dic[user] = 0
    #print(id_dic)

    for unit in permutations(user_id, len(banned_id)):
        #print(unit)
        if check(unit, banned_id):
            #print(unit)
            if set(unit) not in answer:
                answer.append(set(unit))
    #print(answer)                  
    return len(answer)
