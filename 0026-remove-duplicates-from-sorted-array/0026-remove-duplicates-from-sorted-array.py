class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1, ptr2 = 0, 0
        for ptr2 in range(len(nums)):
            if nums[ptr2] != nums[ptr1]:
                ptr1 += 1
                nums[ptr1] = nums[ptr2]
        return ptr1+1
            
