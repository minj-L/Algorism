# 힌트 보고 풀이
# 숫자들을 나누어서 그 자리 수 만큼의 로마숫자를 표현하면 될거 같았다.
# 그런데 그 나누어진 숫자들이 특정 자리 수 인지를 어떻게 표시해야 할지를 모르겠었다.

class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        i = 0 # 몇 번째 자리 수 인지
        res = [] # saving numbers convert to Roman

        while num > 0:
            n = num % 10

            if 1 <= n <= 3:
                res.append(ones[i] * n)
            elif n == 4:
                res.append(ones[i] + fives[i])
            elif 5 <= n <= 8:
                res.append(fives[i] + ones[i] * (n-5))
            elif n == 9:
                res.append(ones[i]+ones[i+1])
            
            i += 1
            num //= 10
        
        return "".join(res[::-1])