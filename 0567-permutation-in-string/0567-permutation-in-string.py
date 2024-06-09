from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str1 = Counter(s1)
        i = 0
        while i < len(s2) - len(s1) + 1:
            substr = Counter(s2[i: i + len(s1)])
            print(substr)
            if str1 - substr == {}:
                return True
            i += 1
        return False
