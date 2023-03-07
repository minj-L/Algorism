from itertools import combinations

def solution(orders, course):
    answer = []
    dic = {}
    temp = []
    
    for c in course:
        for j in orders:
            items = list(j)
            items.sort()
            comb = list(combinations(items, c))
            #print(comb)
            for z in comb:
                str = ''.join(z)
                if str in dic.keys():
                    dic[str] += 1
                else:
                    dic[str] = 1
        #print(dic)
        if dic != {}:
            max_value = max(dic.values())
            #print(max_value)
            for key, value in dic.items():
                if value == max_value and value >= 2:
                    #print(key)
                    answer.append(key)
                    answer.sort()
        dic.clear()
    #print(answer)    
    
    return answer
