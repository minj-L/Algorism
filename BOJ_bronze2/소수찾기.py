def solution(numbers):
  sosu = 0

  for n in numbers:
    error = 0
    if n > 1:
      for i in range(2, n):
        if n % i == 0:
          error += 1
      if error == 0:
        sosu += 1

  return sosu

print(solution([1,3,5,7])) 
