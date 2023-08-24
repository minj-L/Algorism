# 힌트 열람 대각선을 기준으로 줄을 세어 짝수줄은 분자가 오름차순으로 증기하고
# 홀수줄은 분자가 내림차순으로 줄어든다는 것을 이용하라

num = int(input())

line = 1
while num > line:
    num -= line
    line += 1

if line % 2 == 0:
    a = num
    b = (line - num) + 1
else:
    a = (line - num) + 1
    b = num
print( a, '/' , b, sep='')
print(f'{a}/{b}') # 이런방법도..!