from bisect import bisect_left, bisect_right

# '정렬된 리스트'에서 '값이 특정 점위에 속하는 원소의 개수'를 구할 때 좋다.
def count_by_range(b, left_value, right_value):
    right_index = bisect_right(b, right_value)
    left_index = bisect_left(b, left_value)
    print('right : ', right_index, 'left : ', left_index)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
#right의 index는 8이고 left의 index는 6이니까 이 사이에 있는 값 확인할 때 좋겠구나
