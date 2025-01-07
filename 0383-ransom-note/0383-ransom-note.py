from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        for each in ransomNote:
            if each in available and available[each] > 0:
                available[each] -= 1
            else:
                return False
        return True
            
        