class Solution:
    def partitionString(self, s: str) -> int:
        # highest freq of repeating char = no of unique substrings
        # # sorting nlogn, find max freq
        # # o(n) traverse and consume more memory
        # sorted_str = sorted(s)
        # max_freq = 1
        # # 1 because by default min 1 string should be present
        # curr_freq = 1
        # print("sorted_str ", sorted_str)
        # for i in range(1, len(s)):
        #     if sorted_str[i] == sorted_str[i-1]:
        #         curr_freq += 1
        #         max_freq = max(max_freq, curr_freq)
        #     else:
        #         curr_freq = 1
        # return max_freq
        # # PROBLEM IS continuous substring!

        # traverse O(n) create a new set for every substring
        # if char exists start new substr
        # count this
        unique_c = set()
        substr_count = 1

        for each in s:
            if each in unique_c:
                # start new substr from here
                substr_count += 1
                unique_c = set()
            unique_c.add(each)
        return substr_count


