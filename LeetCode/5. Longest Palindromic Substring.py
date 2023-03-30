class Solution:
    def longestPalindrome(self, s: str) -> str:
        #stack으로 풀면 될 것 같다->아님
        # stack = []

        # for char in s:
        #     stack.append(char)
        #     if 

        #long = ""
        if len(s) <= 1:
            return s
        
        # for i in range(len(s)):
        #     for j in range(len(s), i, -1):
        #         # print(s[i:j][::-1]) s[i에서 j-1만큼의] 배열내용을 뒤집는다는 의미
        #         if len(long) >= j - i:
        #             continue
        #         elif s[i:j] == s[i:j][::-1]:
        #             long=s[i:j]

        # start, length = 0, 0
        # for end in range(len(s)):
        #     # 기존 substring에서 자신만 추가하여 조건 성립 Ex. aaa
        #     if s[end-length:end+1] == s[end-length:end+1][::-1]:
        #         start, length = end-length, length+1
        #     # 기존 substring에서 자신과 앞을 추가하여 조건 성립 Ex. baaab
        #     elif end-length-1 >= 0 and s[end-length-1:end+1] == s[end-length-1:end+1][::-1]:
        #         start, length = end-length-1, length+2

        # return s[start:start+length]

        start, length = 0,0
        for end in range(len(s)):
            # ex aaa인 경우
            if s[end-length:end+1] == s[end-length:end+1][::-1]:
                start, length = end-length, length+1
            elif end-length-1 >=0 and s[end-length-1:end+1] == s[end-length-1:end+1][::-1]:
                start, length = end-length-1, length+2
        return s[start:start+length]
