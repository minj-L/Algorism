#람다로 풀이! JAVA로도 풀어봐야지
def solution(n, arr):
    answer = sorted(arr, key=lambda x : x[1])
    return answer
print(solution(5, [[3, 4],[1,1],[1,-1],[2,2],[3,3]]))
# 테케는 맞았는데 틀렸다고나옴 왜..?

import sys
n=int(sys.stdin.readline())
li=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append([a, b])
li.sort()
for i in li:
    print(i[0], i[1])
