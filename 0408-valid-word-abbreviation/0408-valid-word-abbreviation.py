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
        word_i = 0
        abbr_i = 0

        while abbr_i < len(abbr) and word_i < len(word):
            abbr_char = abbr[abbr_i]
            # print(word_i, word[word_i], " and ", abbr_char)

            if abbr_char.isalpha():
                # just compare corr chars
                if word[word_i] != abbr_char:
                    return False
                abbr_i += 1
                word_i += 1
            else:
                # it's number - assumption
                num = 0
                while abbr_i < len(abbr) and abbr[abbr_i].isdigit():
                    num = num *10 + int(abbr[abbr_i])
                    if num == 0:
                        return False
                    abbr_i += 1
                
                # print("word ", word_i, word[word_i], " num = ", num)
                # now check word
                if word_i + num > len(word):
                    return False
                word_i += num

        if abbr_i < len(abbr) or word_i < len(word):
            return False
        return True

