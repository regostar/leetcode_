class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # result option len is len oif digits str
        # 1 is not given
        # max digits str len = 4
        # 4^4 max => m^n
        #  backtracking
        if len(digits) == 0:
            return []
        
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                combos.append("".join(path))
                return
                
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
                # backtrack by removing the letter before moving onto the next 

        combos = []
        backtrack(0, [])
        return combos
        