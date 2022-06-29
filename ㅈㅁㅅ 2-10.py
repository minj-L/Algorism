n = int(input("대기실에 몇개의 의자가 있나요 : "))

if n%2 == 0:
  min = n - (n-2)
  print("최소: ", min)
  max = n//2
  print("최대: ", max)
  
if n%2 == 1:
  min = n - (n-2)
  print("최소: ", min)
  max = (n//2) + 1
  print("최대: ", max)
