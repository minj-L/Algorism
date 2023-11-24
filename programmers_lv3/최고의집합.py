# https://bladejun.tistory.com/68
"""
단순히 문제에서 요구하는 조건을 모두 구현하는 것이 아니라
어떻게 짧고 효율적인 방법으로 답을 도출할 것인지를
생각해야 한다는 것을 깨달은 문제  
"""
# S의 조합을 찾는 방법을 모르겠다.
"""
-> 조합을 찾을 필요가 없었다 우리가 필요한 건
S가 되는 집합 들의 곱 중 가장 큰 곱을 찾는 것,
그러니 집합내의 숫자들이 가장 큰 집합을 찾아내는 
코드를 작성해야 한다.
"""

def solution(n, s) :
    answer = []
    if n > s:
        answer.append(-1)
        return answer
    
    # divmod() 함수 s // n의 몫과 나머지를 모두 구해준다.
    quo, rem = divmod(s, n)

    answer = [quo] * n
    for i in range(rem):
        answer[i] += 1
    return sorted(answer)
print(solution(2, 8))