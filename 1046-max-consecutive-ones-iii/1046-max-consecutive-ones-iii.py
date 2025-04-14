class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # it need not be the longest chain of 1s + adding k 0s
        # it can be multiple small 1s which join to form 1 big 
        # we can do a sliding window approach
        # move to right when the no of 0s encountered is < k
        # move left when you encounter a arr[right] = 0, until the next 0
        # we are skipping first 0 in the sliding window
        n = len(nums)
        left = 0
        right = 0
        zeros_in_window = 0
        max_len = 0
        # max cons 1s with k 0 flips
        while right < n and left <= right:
            if nums[right] == 1:
                right += 1
                cur_len = right - left
                max_len = max(max_len, cur_len)
            else:
                # == 0
                zeros_in_window += 1
                if zeros_in_window > k:
                    # move left until next 0
                    while nums[left] != 0 and left <= right:
                        left += 1
                    # skip 0
                    left += 1
                    # we already checked len in last step
                    zeros_in_window -= 1
                    # revert since we removed one 0

                right += 1
                cur_len = right - left
                max_len = max(max_len, cur_len)
        return max_len





        