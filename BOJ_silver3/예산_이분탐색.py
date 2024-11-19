N = int(input())

buget = list(map(int, input().split()))

M = int(input())

# 예산 초기금액
init = 0
max_buget = max(buget)

while init <= max_buget:
    mid = (init + max_buget) // 2

    total = 0
    for b in buget:
        if b > mid:
            total += mid
        else:
            total += b
    if total <= M:
        init = mid + 1
    else:
        max_buget = mid - 1
print(max_buget)