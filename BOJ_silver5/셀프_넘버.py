# arr = [a for a in range(1, 10001)]

# for i in range(1, 10001):
#     if len(str(i)) == 2:
#         n = i + (i//10) + (i%10)
#     if len(str(i)) == 3:
#         n = i + (i//1000) + ((i//1000) // 100) + (((i//1000) // 100) % 10)
#     if len(str(i)) == 4:
#         n = i + (i//10000) + ((i//10000) // 1000) + (((i//10000) // 1000) // 100) + ((((i//10000) // 1000) // 100) % 10)
#     if n > 10000:
#         continue
#     arr.remove(n)
#     #print(n)

# print(arr)

# for b in arr:
#     print(b)

num_set = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)
self_num = sorted(num_set - generated_num)
for i in self_num:
    print(i)