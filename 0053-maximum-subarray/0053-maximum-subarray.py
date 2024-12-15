class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force O(n^3)
        # attempt in O(n)
        
        # accept if sum so far > curr
        # else sum so far = curr
        
        sum_so_far = float('-inf')
        max_sum_seen = float('-inf')
        
        i = 0
        while i < len(nums):
            if nums[i] > sum_so_far + nums[i]:
                sum_so_far = nums[i]
            else:
                sum_so_far += nums[i]
            max_sum_seen = max(max_sum_seen, sum_so_far)
            i += 1
        return max_sum_seen
                
        