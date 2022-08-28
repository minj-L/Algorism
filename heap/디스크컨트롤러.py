import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장한다.
        for j in jobs:
            if start < j[0] <= now: #작업 시간이 now보다 작거나 같다면 
                heapq.heappush(heap, [j[1], j[0]]) #heap에 넣는데, 
                #[작업 소요시간, 작업 요쳥 시점]으로 요소의 앞 뒤를 바꿔 넣어준다.

        # 처리할 작업이 있는 경우
        if len(heap) > 0:
            cur = heapq.heappop(heap) #힙에 저장된 job을 꺼내 cur에 넣고
            start = now 
            now += cur[0] #작업 소요시간을 지금 시간으로 바꿔준다.
            answer += now - cur[1] 
            #작업 총 소요시간을 구하기 위해 answer에 더해 줌
            i += 1
        else :
            now += 1
    return answer // len(jobs)
print(solution([[0, 3], [1, 9], [2, 6]]))
