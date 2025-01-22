class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                    


        return max(LIS)