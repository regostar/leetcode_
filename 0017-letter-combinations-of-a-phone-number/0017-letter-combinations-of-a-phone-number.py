class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_to_char = { '2': "abc", 
            '3': "def", 
            '4': "ghi", 
            '5': "jkl", 
            '6': "mno", 
            '7': "pqrs", 
            '8': "tuv", 
            '9': "wxyz"
            }
        def back_track(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
            for c in digits_to_char[digits[i]]:
                back_track(i + 1, cur_str + c)
                # need to take one of them for sure
        if digits:
            back_track(0, "")
        return res
        
        