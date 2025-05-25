class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0  # count of zeros in the current window
        max_length = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            # If there are more than k zeros in the window,
            # move the left pointer until the window is valid again.
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # Update the maximum window length found.
            max_length = max(max_length, right - left + 1)
        
        return max_length
