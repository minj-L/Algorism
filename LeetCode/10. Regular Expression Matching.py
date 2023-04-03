class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s_list = list(s)
        # p_list = list(p)

        # if len(s) != len(p):
        #     return False
        
        # if "*" in p_list:
        #     star_position = p_list.index("*")
        #     print(star_position)
        #     p_list[star_position] = p_list[star_position-1]
        #     print(p_list)
        #     if s_list == p_list:
        #         return True
        
        # if "." in p_list:

        s, p = ' ' + s, ' ' + p #1부터 시작하기 위해 빈칸 생성
        print(s, p)
        lenS, lenP = len(s), len(p)
        print(lenS, lenP)
        dp = [[0] * (lenP) for i in range(lenS)]
        print(dp)
        dp[0][0] = 1 #앞의 빈칸 처리

        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]
        print(dp)
        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i -1][j - 1]
                    print(dp)
                elif p[j] == "*": #dp[i][j-2]는 정규식 p 내에 있는 문자를 제외한 s내의 글자만 들어가야 s와 p가 같아지며 True가 된다. 해당 문자가 0번 나타났을 경우
                    dp[i][j] = dp[i][j - 2] or int(dp[i - 1][j] and p[j - 1] in {s[i], '.'})
                    #p[j-1] 즉 * 앞에 있는 문자가 s[i]나 . 이고 dp[i-1][j]는 현재 j의 위치에서 s 한칸 앞에 있는 숫자가 True이면 그것을 dp[i][j]에 대입한다.
                    print(dp)
        print(dp)
        return bool(dp[-1][-1])
            


        
