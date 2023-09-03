num_list = set(i for i in range(1, 10001))
not_self_num = set()

for n in num_list:
    for i in str(n):
        n += int(i)
    not_self_num.add(n)
self_num = sorted(num_list-not_self_num)

for s in self_num:
    print(s)