# 18 5 3개 3 1개 = 4
# 9 3 3개 = 3
# 16 19 22
# 말고 예외가 또 뭐있는데 7...-1이 나와야하는데,,3나옴

# sugar = int(input())

# res = 0

# div_sugar = sugar // 5
# remain_sugar = sugar % 5

# if div_sugar <= 0:
#     print(-1)
# else:
#     res += div_sugar

#     if remain_sugar < 3 :
#         res += remain_sugar
#     else:
#         div_sugar_3 = remain_sugar // 3
#         res += div_sugar_3
#         remain_sugar_3 = remain_sugar % 3
#         res += remain_sugar_3

#     print(res)

sugar = int(input())

if sugar % 5 == 0:
    print(sugar // 5)
else:
    res = 0
    while sugar > 0:
        sugar -= 3
        res += 1
        if sugar % 5 == 0:
            res += sugar // 5
            print(res)
            break
        elif sugar == 1 or sugar == 2:
            print(-1)
            break
        elif sugar == 0:
            print(res)
            break
