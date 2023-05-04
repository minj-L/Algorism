import sys
input = sys.stdin.readline
x,y,w,h = map(int,input().split())
result = [(x-0), (y-0), (w-x), (h-y)]
print(min(result))
