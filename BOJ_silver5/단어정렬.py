def solution(words):
    answer = 0
    set_word = list(set(words))
    print(set_word)

    sort_word = []
    for s in set_word:
        sort_word.append((len(s), s))
    print(sort_word)

    res = sorted(sort_word)

    return res

print(solution(['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more']))
