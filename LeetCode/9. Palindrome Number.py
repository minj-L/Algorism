class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        if x_list == x_list[::-1]:
            return True
        else:
            return False
