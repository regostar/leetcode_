class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()

        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                tot = nums[i] + nums[lo] + nums[hi]
                if abs(target-tot) < abs(diff):
                    diff = target-tot
                if tot < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff