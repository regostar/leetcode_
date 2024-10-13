class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 pointer approach
        # slow ptr will stop at next zero
        # fast ptr after 0, non zero 
        slow = 0
        fast = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # swap with fast
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            

        