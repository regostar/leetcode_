# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Simple way is +1 and -1 but this is linear time complexity
        optimized soln would be to use binary search
        """
        low = 1
        high = n
        # max is n because user picks a no from 1 to n (high)
        # mid = (low + high) // 2
        
        # to avoid roll over 
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                # lower
                low = mid + 1
            elif res == -1:
                # greater
                high = mid - 1
            else:
                return -1
        return -1






        # current_guess = n
        # res = n
        # while res != 0:
        #     res = guess(current_guess)
        #     if res == -1:
        #         current_guess = current_guess - 1
        #     elif res == 1:
        #         current_guess += 1

        # return current_guess
        