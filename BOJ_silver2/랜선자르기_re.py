k, n = map(int, input().split())

len_list = []
for _ in range(k):
    len_list.append(int(input()))

init = 1
max_length = max(len_list)

while init <= max_length:
    mid = (init + max_length) // 2

    real_len = 0
    for l in len_list:
        real_len += l // mid

    if real_len >= n:
        init = mid + 1
    else:
        max_length = mid - 1

print(max_length)