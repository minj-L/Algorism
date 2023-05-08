import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())

r_num1 = num1
r_num2 = num2

res = []

# 최대공약수
while num2 > 0:
    tmp = num1
    num1 = num2
    num2 = tmp % num2
res.append(num1)
    
# 최소공배수
lcm = (r_num1 * r_num2) // num1
res.append(lcm)

for i in res:
    print(i)
#
