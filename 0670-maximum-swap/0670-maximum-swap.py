class Solution:
    def maximumSwap(self, num: int) -> int:
        # find max digit in number and swap to Most significant digit
        # 29973
        # which 9 do we swap ?
        # 92973 or 99273 ?
        # we find the max digit found located in the rightmost
        # 99736
        # max will be 99763
        # so we are not only finding the max but we need to make one swap
        # such that max from right goes to left

        max_digit = "0"
        string_num = list(str(num))
        loc = -1
        swap_i = swap_j = -1
        for i in reversed(range(len(string_num))):
            # max
            if string_num[i] > max_digit:
                max_digit = string_num[i]
                loc = i
            # swap
            if string_num[i] < max_digit:
                swap_i, swap_j = i, loc
        string_num[swap_i], string_num[swap_j] = string_num[swap_j], string_num[swap_i]
        
        return int("".join(string_num))
            
            