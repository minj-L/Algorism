n, k = map(int, input().split())

len_line = []
for i in range(n):
    len_line.append(int(input()))

# 초기 값
init = 1
max_num = max(len_line)

while init <= max_num:
    mid = (init + max_num) // 2

    real_lan = 0
    for i in len_line:
        real_lan += i // mid
    if real_lan >= k:
        init = mid + 1
    else:
        max_num = mid - 1
print(max_num)

"""
6개로 만들어라
28 13:2 52 13 : 4
아 내가 14로 잡아놓고 개수대로 안나올거 같으니까 하나씩 쭐인거랑 같은 맥락이구나
24 14: 2 52 14 : 3 5 5개 나왔으니 더 작게 잘라야 겠다
802
743
457
539
"""