from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        pali_len = 0
        odd_exists = False
        key_freq = Counter(s)
        print(key_freq)
        for key, freq in key_freq.items():
            if freq % 2 != 0:
                odd_exists = True
                if freq > 1:
                    pali_len += freq ^ 1
            else:
                pali_len += freq
        if odd_exists:
            pali_len += 1
        return pali_len