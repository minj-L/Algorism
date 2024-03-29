class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        
        # save_s = []
        # save_ss = []
        # for S in s:
        #     if S not in save_s:
        #         save_s.append(S)

        # print(save_s)

        left = 0
        used = {}

        for right, char in enumerate(s):
            if char in used and left <= used[char]:
                left = used[char] + 1
            else:
                answer = max(answer, right - left + 1)
            used[char] = right

        return answer

    # used two pointer
    # enumerate() (0, somthing), (1, somthing), (2, somthing) 형태의 집합을 만들어줌
