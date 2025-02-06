class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # after sorting, the middle element will always be the majority element because
        # it's given that maj ele freq > n/2
        return nums[len(nums)//2]
        