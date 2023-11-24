n = int(input())

# arr = []
# one = 0

# for i in range(n, 0, -1):
#     while i > 1:
#         if i // 2 == 1:
#             one += 1
#         if i % 2 == 1:
#             one += 1
#         i = i // 2
#     arr.append(one)
#     one = 0
# print(arr)

ans = [0] * (n + 1)
offset = 1
for i in range(1, n + 1):
    if offset * 2 == i:
        offset *= 2
    ans[i] = ans[i - offset] + 1

print(ans)
            
