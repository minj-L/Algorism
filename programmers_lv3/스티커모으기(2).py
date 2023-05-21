def solution(sticker):
    answer = 0

    odd_sticker = []
    even_sticker = []
    
    for index in range(0, len(sticker)):
        if index % 2 == 1:
            odd_sticker.append(sticker[index])
        else:
            even_sticker.append(sticker[index])
            
    return max(sum(odd_sticker), sum(even_sticker))
# => 실패! 헤헷 바부

def solution(sticker):
    answer = 0

    if len(sticker) <= 3:
        return max(sticker)
    
    # 맨 앞의 스티커를 뗄 경우
    dp1 = [0 for _ in range(len(sticker))]
    # 맨 앞의 스티커를 떼지 않는 경우
    dp2 = [0 for _ in range(len(sticker))]
    
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
        
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])
    return max(max(dp1), max(dp2))
#
