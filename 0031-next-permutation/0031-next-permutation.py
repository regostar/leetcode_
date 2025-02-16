class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        # find the pivot
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # 1 2 3 4 5
        # 1 2 3 5 4
        # 1 2 4 3 5
        if i >= 0: 
            # pivot exists which means it is has next
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
                # find number in right side which is less than this
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)
    
    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp