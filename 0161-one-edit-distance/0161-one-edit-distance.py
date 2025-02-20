class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # abcde
        # abde
        # len differ by more than 1 - false
        # if len are equal, then one update 
        # if len are unequal then insert in one or delete in other is same
        s_len = len(s)
        t_len = len(t)
        if abs(s_len - t_len) > 1:
            return False
        
        for i in range(min(s_len, t_len)):
            if s[i] != t[i]:
                if s_len == t_len:
                    return s[i+1:] == t[i+1:]
                elif s_len < t_len:
                    return t[i+1:] == s[i:]
                else:
                    return s[i+1:] == t[i:]
        
        # length is same but not matching taken care
        # length is different == 1 '
        # we only iterted toll min(s_len, t_len) what if last element is different?
        return abs(s_len - t_len) == 1
        # only 1 char is allowed to be different

        