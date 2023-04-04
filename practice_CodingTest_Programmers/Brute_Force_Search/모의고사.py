def solution(answers):
    
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    c1, c2, c3 = 0, 0, 0
    
    for a in range(len(answers)):
        k1 = a % 5
        k2 = a % 8
        k3 = a % 10
        
        if answers[a] == num1[k1]:
            c1 += 1
        if answers[a] == num2[k2]:
            c2 += 1
        if answers[a] == num3[k3]:
            c3 += 1
    
    max_correcter = max(c1, c2, c3)
    answer = []
    if max_correcter == c1:
        answer.append(1)
    if max_correcter == c2:
        answer.append(2)
    if max_correcter == c3:
        answer.append(3)
            
    return answer
