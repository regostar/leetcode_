class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # when you encounter a number, 
        # get the entire number until we reach a char
        # now traverse that many indices in the corr. str
        # next char should match in both strings, else FALSE
        # if matched then proceed with next 
        # if you reach end in one and other still have some chars to traverse
        # ret = FALSE
        # edge cases - if there is leading 0, then while converting to num
        # it gets taken care
        # if there is on0ly 0 
        # then we return FALSE

        # edge case - it cannot start with no
        
        # initialize both indexes
        abbr_i = 0
        str_i = 0
        num = 0
        num_started = False
        start_char = None

        while abbr_i < len(abbr) and str_i < len(word):
            if abbr[abbr_i].isdigit():
                num_started = True
                while abbr_i < len(abbr) and abbr[abbr_i].isdigit():
                    num = num * 10 + int(abbr[abbr_i])
                    if num == 0:
                        return False
                    abbr_i += 1
                
                # now check with the word
                while num > 0:
                    if str_i >= len(word):
                        return False
                    str_i += 1
                    num -= 1

            else:
                # traverse both
                if word[str_i] != abbr[abbr_i]:
                    return False
                abbr_i += 1
                str_i += 1

        if abbr_i < len(abbr) or str_i < len(word):
            return False
        return True

        