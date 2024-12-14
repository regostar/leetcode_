class Solution:

    def __init__(self):
        self.res = ""
        self.res_len = 0

    def expand_check(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > self.res_len:
                self.res = s[l: r + 1]
                self.res_len = r - l + 1
            l -= 1
            r += 1
    
    def longestPalindrome(self, s: str) -> str:
        # brute force -
        # O(n^2) check every combo and O(n) see if it's a palindrome => O (n^3)
        # 2 pointer approach start from center
            

        for i in range(len(s)):
            # consider this as center and traverse checking for odd pali and even pali
            
            # odd pali check
            l, r = i, i
            # i = 2, l = 1, r = 3, len = 3 so r - l + 1
            self.expand_check(l, r, s)
            
            # for even
            l, r = i, i + 1
            self.expand_check(l, r, s)

        return self.res