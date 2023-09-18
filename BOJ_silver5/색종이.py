num = int(input())

base = [[0] * 100 for _ in range(100)]

for i in range(num):
    n1, n2 = map(int, input().split())

    for i in range(n2, n2 + 10):
        for j in range(n1, n1 + 10):
            base[i][j] = 1

res = 0

for k in range(100):
    res += base[k].count(1)
print(res)
