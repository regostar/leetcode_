class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        # case 1
        # nums[0] > lower
        # case 2
        # nums[-1] < high
        # ==
        ranges = []
        n = len(nums)
        if not nums:
            return [[lower, upper]]
        if nums[0] > lower:
            ranges.append([lower, nums[0] - 1])
        for i in range(0, n - 1):
            if nums[i + 1] - nums[i] > 1: 
                ranges.append([nums[i] + 1, nums[i+1] - 1])
        if nums[n - 1] < upper:
            ranges.append([nums[n-1] + 1, upper])
        return ranges
                
        