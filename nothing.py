def solution(S):
    n = len(S)

    max_len = 0

    for i in range(n // 2):
        len1 = i + 1
        count1 = S[:len1].count('<') + S[:len1].count('?')
        count2 = S[len1:].count('>') + S[len1:].count('?')
        if count1 == count2:
            len2 = n - len1
            if (len1 + len2) % 2 == 0: # 추가된 부분
                max_len = max(max_len, 2 * min(len1, len2))
    return max_len
