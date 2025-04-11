class Solution:
    def confusingNumber(self, n: int) -> bool:
        # 0 , 6
        # all digits in the num must be rotatable
        # simply parse each digit, if it is in the non rotate list then return fals
        non_rotate = {2, 3, 4, 5, 7}
        rotation = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        num = n
        new_num = 0
        while num:
            digit = num % 10
            if digit in non_rotate:
                return False
            new_num = new_num * 10 + rotation[digit]
            num //= 10
        
        return new_num != n
