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

number_set = set(range(1, 10001)) 
# [] 배열에서 수생성 하는 것과 set의 차이
# 여기서는 값을 더 쉽게 구하기 위해 집합 함수를 사용한 것이다.
not_self_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    not_self_num.add(i)

self_num = sorted(number_set - not_self_num)

for i in self_num:
    print(i)