class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to str and check from middle
        # but wh extra space, simply reverse num and compare
        # but for -ve nos - all -ve nos are not pali
        # edge case - 1000 and 0001
        if x < 0:
            return False
        
        reversed_num = 0
        num = x
        while num:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        return reversed_num == x