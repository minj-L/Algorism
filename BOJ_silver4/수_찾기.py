#이진탐색
n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

a.sort() # 1 2 3 4 5

for num in arr:
    lt, rt = 0, n - 1
    exist = False

    while lt <= rt:
        mid = (lt+rt) // 2
        if num == a[mid]:
            exist = True
            print(1)
            break
        elif num > a[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    
    if not exist:
        print(0)
