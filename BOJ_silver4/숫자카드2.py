def binary_search(array, target, lt, rt):
    if lt > rt:
        return 0
    mid = (lt + rt) // 2
    if array[mid] == target:
        return cnt.get(target)
    elif array[mid] > target:
        return binary_search(array, target, lt, mid-1)
    else:
        return binary_search(array, target, mid+1, rt)

n = int(input())
arr = sorted(list(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split()))

cnt = {}
for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
print(cnt)

for i in arr2:
    print(binary_search(arr, i, 0, len(arr)-1), end=' ')
