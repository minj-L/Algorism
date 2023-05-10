# while True:
#     n = input()
#     if n[0] == '0':
#         continue
#     for i in range((len(n) // 2) + 1):
#         if n[i] != n[len(n)-1-i]:
#             print("no")
#             break
#         else:
#             print("yes")
#             break

while True:
    n = input()
    
    if n == '0':
        break

    if n == n[::-1]: # [::-1] 은 거꾸로 뒤집는다는 의미
        print('yes')
    else:
        print('no')
