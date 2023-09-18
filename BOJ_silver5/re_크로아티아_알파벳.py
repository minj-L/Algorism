# 파이썬의 replace는 문자열을 변경하는 함수이다. 이를 이용했어야 했음

cro_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()

for c in cro_words:
    words = words.replace(c, '*')
    print(words)
#print(len(words))