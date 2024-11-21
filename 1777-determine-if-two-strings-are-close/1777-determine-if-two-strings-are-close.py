from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # length should be same
        if len(word1) != len(word2):
            return False
        # basically char and freq should be same - Na
        # no of distinct chars and frequencies list should be same
        char_count_1 = Counter(word1)
        char_count_2 = Counter(word2)
        if len(char_count_1.keys()) != len(char_count_2.keys()):
            return False
        print(char_count_1)
        # distinct characters should be same
        for each_char in char_count_1.keys():
            if each_char not in char_count_2:
                return False
        sorted_freq1 = list(char_count_1.values())
        sorted_freq1.sort()
        sorted_freq2 = list(char_count_2.values())
        sorted_freq2.sort()
        if len(sorted_freq1) != len(sorted_freq2):
            return False
        for i in range(len(sorted_freq1)):
            if sorted_freq1[i] != sorted_freq2[i]:
                return False
        return True


        

        