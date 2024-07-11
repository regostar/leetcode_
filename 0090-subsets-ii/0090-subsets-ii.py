class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i: int, subset: List=None):
            if i >= len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
            # this subset does not have current element
        backtrack(0, [])
        return res

        