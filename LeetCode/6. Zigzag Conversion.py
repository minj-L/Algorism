class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # save_string = [[] for _ in range(numRows)]
        # res = ''        
        # downflag = True
        # idx = 0

        # for i in s:
        #     save_string[idx].append(i)
        #     print(save_string)

        #     if idx == 0:
        #         downflag = True
        #     elif idx == (numRows - 1):
        #         downflag = False
            
        #     if downflag:
        #         idx += 1
        #     else:
        #         idx -= 1
        # print(save_string)

        # for i in list(map(''.join, save_string)):
        #     res+=i

        store = [[] for _ in range(numRows)]
        res = ''
        downFlag = False

        idx = 0
        for i in s:
            store[idx].append(i)

            if idx == 0:
                downflag = True
            elif idx == (numRows - 1):
                downflag = False
            
            if downflag:
                idx += 1
            else:
                idx -= 1

        for i in list(map(''.join, store)):
            res += i

        print(store)
        
        return res
