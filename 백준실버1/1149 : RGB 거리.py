#dynamic programing 이전 계산값을 저장해서 다음 계산에 사용
#앞에서 부터 최소 값을 저장해 나가며, 모든 집을 칠했을 때의 최소값을 구하는 문제
#https://this-programmer.tistory.com/446
#https://zidarn87.tistory.com/272

house_num = int(input())
price = [list(map(int, input().split())) for _ in range(house_num)]
for i in range(1, house_num):
    price[i][0] = min(price[i - 1][1], price[i - 1][2]) + price[i][0]
    price[i][1] = min(price[i - 1][0], price[i - 1][2]) + price[i][1]
    price[i][2] = min(price[i - 1][0], price[i - 1][2]) + price[i][2]
print(min(price[house_num]))
