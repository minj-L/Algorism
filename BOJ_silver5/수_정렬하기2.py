import sys

arr = []
n = int(input())
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for j in arr:
    print(j)
