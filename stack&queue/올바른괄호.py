
# 1차 시도
# def solution(s):
#     stack = []
#     cnt1 = 0
#     cnt2 = 0

#     for i in range(len(s)):
#         stack.append(s[i])
#         if stack[i] == '(':
#             cnt1 += 1
#         elif stack[i] == ')':
#             if i == 0:
#                 return False
#             cnt2 += 1
#     if cnt1 == cnt2:
#         return True
#     else:
#         return False

# print(solution(")()("))

#2차 시도
stack = []

for i in s:
    if i == '(':
        stack.append(i)
    else:
        if stack == []:
            print("false")
            break
        else:
            stack.pop()
print(stack == [])
