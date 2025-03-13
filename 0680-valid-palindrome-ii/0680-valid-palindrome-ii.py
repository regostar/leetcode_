class Solution:
    def is_pali(self, s: str, l: int, r: int)-> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l+= 1
            r-=1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        # 2 pointer approach
        left = 0
        right = len(s) - 1
        
        
        while left < right:
            if s[left] != s[right]:
                # check by trying both options if pali now
                # if we find result return
                left_option = self.is_pali(s, left+1, right)
                right_option = self.is_pali(s, left, right-1)
                return left_option or right_option
            
            left += 1
            right -= 1
        
        return True
            
            
        
        