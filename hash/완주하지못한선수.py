def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for part in participant:
        hashDict[hash(part)] = part #파이썬 hash(some)은 some에 hash값을 부여해 준다.
        sumHash += hash(part)
    
    for comp in completion:
        sumHash -= hash(comp)
    
    return hashDict[sumHash]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
