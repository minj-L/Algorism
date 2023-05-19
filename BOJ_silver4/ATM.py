n = int(input())
time = list(map(int, input().split()))

time = sorted(time)

for t in range(len(time)-1):
    time[t + 1] = time[t] + time[t + 1]

print(sum(time))
