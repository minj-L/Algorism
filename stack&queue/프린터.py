def solution(priorities, location):
    answer = 0
    while True:
        m = max(priorities) # 리스트에서 가장 큰수
        for i in range(len(priorities)): # 리스트를 처음부터 확인한다 
            if m == priorities[i]: # 만약 가장 큰 수와 리스트의 요소와 일치 시
                answer += 1 # answer에 1 추가 
                priorities[i] = 0 # 프린트한 요소는 0으로 표시 
                m = max(priorities) #다시 for문안에서 큰수와 priorites를 비교하기 위해 큰수를 구함
                if i == location: # 만약 location과 i가 일치하면 answer을 반환
                    return answer
print(solution([1,1,9,1,1,1], 0))
