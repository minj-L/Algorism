import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        print(s)
        # numbers=re.findall(r'\d+', s)
        # print(numbers)
        # if s.find('-') != -1:
        #     return int(s)

        # return int(numbers[0])

        if s == "":
            return 0
        else:
            numbers=re.findall(r'^[-+]?[0-9]+', s)

            if len(numbers) == 0:
                return 0
            else:
                number = int(numbers[0])
                if number > pow(2,31) - 1:
                    number = pow(2,31) - 1
                elif number < pow(2,31) * (-1):
                     number = pow(2,31) * (-1)
        return number
