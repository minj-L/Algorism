def solution(S):
    nested = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}  
    nest = []
    for s in S:
        if nested[s] > 0:
            nest.append(s)
        if nested[s] < 0:
            if len(nest) == 0: return 0
            t = nest.pop()
            if abs(nested[t]) != abs(nested[s]):
                return 0
    if len(nest) != 0: return 0
    return 1
print(solution("{[()()]}"))

#이것도 보고 품 원리 파악하고 다시 원리에 따라 풀이
