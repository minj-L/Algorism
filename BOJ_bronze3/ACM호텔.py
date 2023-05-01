import sys
N = int(sys.stdin.readline())

for n in range(N):
    h, w, n = map(int, input().split())

    floor = n % h
    room = (n // h) + 1

    #floor가 나누어 떨어지는 경우 202, 303 이런 경우
    if floor == 0:
        floor = h
        room -= 1
    print(floor * 100 + room)
