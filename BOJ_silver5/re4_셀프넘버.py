num_list = {i for i in range(1, 10001)}
#num_list = {33}
not_self_num = set()

for i in num_list:
    for s in str(i):
        i += int(s)
    not_self_num.add(i)

self_num = sorted(num_list - not_self_num)
#print(sorted(self_num))

for s in self_num:
    print(s)
