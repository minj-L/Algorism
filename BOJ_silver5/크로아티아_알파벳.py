# c=c=를 처리하지 못함
cro_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
word_cnt = 0

for c in cro_words:
    if (c in s) == True:
        word_cnt += 1
        s=s.replace(c , '')
len_remain_word = len(s.replace(' ', ''))

print(word_cnt + len_remain_word)
print(word_cnt + len(s))

# 이 풀이를 보고 살기가 싫어졌다.
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = 'c=c='

# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))