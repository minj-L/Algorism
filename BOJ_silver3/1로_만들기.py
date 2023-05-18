#DP BottomUp 풀이
#https://bio-info.tistory.com/159 참고
x = int(input())

dp = [0] * (x + 1) #1부터 시작하는거 맞추기 위해 +1 함

#d[1]은 0으로 1이 1로 되는데 필요한 연산은 0회이기 때문입니다.
#d[2]은 2가 1로 되는데 필요한 연산은 1회
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1 # +1은 연산을 진행한 횟수이다

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[x])
