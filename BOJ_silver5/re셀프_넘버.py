
num_list = set(i for i in range(1, 10001))
not_self_num = set()

for n in range(1, 10001):
    for t in str(n):
        n += int(t)
    not_self_num.add(n)

self_num = num_list - not_self_num
sorted_self_num = sorted(self_num)

for s in sorted_self_num:
    print(s)