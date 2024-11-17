from collections import defaultdict

class Solution:
    def appealSum(self, s: str) -> int:
    
        total_appeal = 0
        last_occurrence = {}
        current_appeal = 0

        for i, char in enumerate(s):
            if char in last_occurrence:
                current_appeal += (i - last_occurrence[char])
            else:
                current_appeal += (i + 1)
            
            total_appeal += current_appeal
            last_occurrence[char] = i

        return total_appeal
