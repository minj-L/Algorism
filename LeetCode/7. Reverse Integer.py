class Solution:
    def reverse(self, x: int) -> int:
        #print(len(str(x)))
        # if len(str(x)) == 1:
        #     return x

        # x_list = list(str(x))

        # if x < 0:
        #     x_list = x_list[1:]
        #     x_reverse = x_list[::-1]
        #     x_res = '-'+''.join(x_reverse)
        #     return int(x_res)
        # elif len(str(x)) == 1:
        #     return x
        # elif '0' in x_list:
        #     x_list = str(x).strip("0")
        #     #print(x_list)
        #     x_reverse = x_list[::-1]
        #     x_res = ''.join(x_reverse)
        #     return int(x_res)
        # elif x >= 0:
        #     x_reverse = x_list[::-1]
        #     x_res = ''.join(x_reverse)
        #     return int(x_res)

        if x>0: #Positive
            value=int(str(x)[::-1]) #reversed
        else: #Negative and zero
            value=-1*int(str(x*-1)[::-1])  #reversed
        
        if value not in range(-2**31,2**31): #Overflow 
            value=0
        
        return value
