# 틀렸습니다.
# room_num = input()
# saving_num = []
# num_set = 1

# for r in room_num:
#     if r in saving_num:
#         num_set += 1
#     saving_num.append(r)

# six = saving_num.count('6')
# nine = saving_num.count('9')
# sn_sum = six + nine

# if (sn_sum % 2) == 0 and sn_sum > 1:
#     num_set -= (sn_sum // 2)
# elif (sn_sum % 2) != 0 and sn_sum > 1:
#     num_set -= (sn_sum % 2)

# print(num_set)
    
n = input()

number = [0] * 10

for i in str(n):
    if i == '6' or i == '9':
        if number[6] == number[9]:
            number[6] += 1
        else:
            number[9] += 1
    else:
        number[int(i)] += 1
print(max(number))