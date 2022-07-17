#s = "aabbaccc"

def solution(s):
    answer = len(s)
    # 1개 단위(step) 부터 압축 단위를 늘려가며 확인한다.
    #압축 단위 아 반 이상 되면 더 이상 압축할 수 있는 단위가 아니니까 반 까지만 세는구나
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        # 단위(step) 크기 만큼 증가시키며 이전 문자열과 비교한다.
        for j in range(step, len(s), step): #step 부터 len(s)까지 step씩 증가
            if prev == s[j: j + step]:
                count += 1
            
            else:
                #만약 count가 2 이상이면 2aa 이런형태로 쓰고 아니라면 a 이런 형태로 써라
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >=2 else prev

        answer = min(answer, len(compressed))
    return answer
print(solution("xababcdcdababcdcd"))

#이분꺼 보고 풀이 함 내일 다시 
