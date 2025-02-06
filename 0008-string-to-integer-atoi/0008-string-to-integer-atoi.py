class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        num = 0
        sign = '+'
        max_limit = 2**31 -1
        min_limit = -2**31
        
        index = 0
        
        # remove whitespaces
        while index < n and s[index] == " ":
            index += 1
            
        # check for sign
        if index < n and s[index] == '-':
            sign = '-'
            index += 1
        elif index < n and s[index] == '+':
            index += 1
        print("sign ",  sign)
        # No need to remove 0s as 0* 10 = 0 we can do computation as long as it is digit
        for j in range(index, len(s)):
            each = s[j]
            # if each.isdigit():
            if each >= '0' and each <='9':
                # print("digit ", int(each))
                # print(" num = ", num)
                # valid no
                # num * 10 > 2^31 -1 
                if (num >= max_limit / 10 or num * 10 >= max_limit - int(each)) and sign == '+':
                    # round off 
                    num = max_limit
                    return num
                # num * 10 <= -2^31
                elif sign == '-' and (-num<= min_limit/10 or  -num * 10 <=min_limit +int(each)):
                    num = min_limit
                    return num                    
                num = num * 10 + int(each)
            else:
                break

        if sign == '-':
                return -num
        return num
        
            
        
        