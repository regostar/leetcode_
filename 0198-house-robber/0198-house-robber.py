class Solution:
    def rob(self, nums: List[int]) -> int:
        # 10 100 10 100 100
        # greedy approach
        # O (n) time 
        # all > 0? yes
        # how long is this ? <= 100
        # we can use extra space
        
        for i in range(1, len(nums)):
            if i == 1:
                nums[i] = max(nums[i], nums[i-1])
            else:
                nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        
        return nums[-1]