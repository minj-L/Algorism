#0824 3회차 풀이

num_list = set(range(1, 10001))
not_self_num = set()

for num in range(1, 10001):
    for n in str(num):
        num += int(n)
    not_self_num.add(num)

self_num = num_list - not_self_num
sorted_self_num = sorted(self_num)

for selfNum in sorted_self_num:
    print(selfNum)
        