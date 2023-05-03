#그냥 조합 구하는 문제였다..
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def n_cal(unknow):
    if unknow == 0 or unknow ==1:
        return 1
    else:
        return unknow * n_cal(unknow-1)

print(n_cal(n) // (n_cal(n-k)*n_cal(k)))
