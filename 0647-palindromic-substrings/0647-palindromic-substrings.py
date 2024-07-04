class Solution:
    def countSubstrings(self, s: str) -> int:
        no = 0
        for i in range(len(s)):
            st,en = i, i
            while st>=0 and en <len(s) and s[st] == s[en]:
                st -= 1
                en += 1
                no += 1
            st, en = i, i + 1
            while st>=0 and en <len(s) and s[st] == s[en]:
                st -= 1
                en += 1
                no += 1
        return no
            

        