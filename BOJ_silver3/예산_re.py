n = int(input())

budget = list(map(int, input().split()))

m = int(input())

start = 0
end = max(budget)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for b in budget:
        if b > mid:
            total += mid
        else:
            total += b
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)