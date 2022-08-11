def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = [0 for _ in range(bridge_length)] #다리길이 만큼의 0으로 된 리스트 생성
    
    while bridge:
        
        answer += 1
        bridge.pop(0) #다리 배열에 가장 앞에 있는 값을 출력
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:  #다리 위에 있는 트럭 무게와 다음에 올 트럭 무개를 더했을 때 총 무게를 초과하지 않으면          
                t = truck_weights.pop(0) # 다음트럭을 꺼내서
                bridge.append(t) #브릿지 리스트에 넣는다
            else:
                bridge.append(0) #근데 만약 넘는다면 그냥 아무것도 꺼내지 않는다.
                 
         
    return answer #브릿지 리스트에서 더 이상 꺼낼 것이 없다면 answer 경과시간을 출력한다.
