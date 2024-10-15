class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 2 possibilities
        # add the number to curr list
        # OR start from this number
        # whichever is maximum
        # greedy approach
        max_sum = -float('inf') 
        # min no as max_sum can be +ve, 0, -ve as well
        cur_sum = 0
        # this resets if we consider only current element
        # else it is cont. sum
        for each in nums:
            cur_sum = max(cur_sum + each, each)
            max_sum = max(max_sum, cur_sum)
        return max_sum
        